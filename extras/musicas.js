// -------------------------------------
// API de música
// -------------------------------------

class HttpExcecao {
    constructor(erroHttp, mensagem) {
        this.erroHttp = erroHttp
        this.mensagem = mensagem
    }
}

const requisitarHttp = async (url, metodo, corpo) => {
    const opcoes = {
        method: metodo,
        mode: 'cors',
    }
    if (corpo) {
        opcoes.headers = {
            'Content-Type': 'application/json'
        }
        opcoes.body = JSON.stringify(corpo)
    }
    let resposta
    try {
        resposta = await fetch(url, opcoes)
    } catch (err) {
        console.error('Deu ruim ', err)
        throw new HttpExcecao(null, 'Deu ruim ' + err)
    }
    if (!resposta.ok) {
        throw new HttpExcecao(resposta.status, 'Erro: ' + resposta.status)
    }
    const dados = await resposta.json()
    return dados
}

const ApiMusica = {
    URL: 'http://localhost:8000/api/musicas/',
    pesquisarTodas: async function () {
        console.log('Pesquisa todas as musicas')
        return requisitarHttp(this.URL, 'GET')
    },
    pesquisarPeloCodigo: async function (codigo) {
        console.log('Pesquisr musica pelo codigo: ', codigo)
        return requisitarHttp(this.URL + codigo, 'GET')
    },
    atualizarPeloCodigo: async function (codigo, musica) {
        console.log('Atualizar pelo codigo: ', codigo, musica)
        return requisitarHttp(this.URL + codigo, 'PUT', musica)
    },
    removerPeloCodigo: async function (codigo) {
        console.log('Removendo pelo código', codigo)
        return requisitarHttp(this.URL + codigo, 'DELETE')
    },
    inserir: async function (musica) {
        console.log('Inserindo nova musica', musica)
        return requisitarHttp(this.URL, 'POST', musica)
    }
}

// -------------------------------------
// Controlador alertas
// -------------------------------------

const paginaHttp = {}

const apresentarAviso = (mensagem, tipo) => {
    tipo = tipo || 'alert-danger'
    const elementoAlerta = document.createElement('div')
    elementoAlerta.innerHTML = (
        `<div class="alert ${tipo} alert-dismissible" role="alert">` +
        '  <div>' +
        mensagem +
        ' </div>' +
        '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Fechar"></button>' +
        '<div>'
    )
    paginaHttp.divAlertasSistema.append(elementoAlerta)
}

const alertarErro = (mensagem) => apresentarAviso(mensagem, 'alert-danger')
const alertarSucesso = (mensagem) => apresentarAviso(mensagem, 'alert-success')

// -------------------------------------
// Controlador painel 
// -------------------------------------

const popularFormulario = (musica) => {
    musica = musica || {}
    paginaHttp.txtNome.value = musica.nome || ''
    paginaHttp.txtArtista.value = musica.artista || ''
    paginaHttp.txtTempo.value = musica.tempo || ''
}

const lerFormulario = () => {
    const nome = paginaHttp.txtNome.value || null
    const artista = paginaHttp.txtArtista.value || null
    let tempo = paginaHttp.txtTempo.value || null
    if (tempo) {
        tempo = parseInt(tempo, 10)
    }
    return { nome, artista, tempo }
}

const salvarRegistro = () => {
    const musica = lerFormulario()
    if (paginaHttp.musica.codigo)
        return atualizarMusica(paginaHttp.musica.codigo, musica)
    return salvarNovaMusica(musica)
}

const atualizarMusica = async (codigoMusica, musica) => {
    try {
        await ApiMusica.atualizarPeloCodigo(codigoMusica, musica)
        alertarSucesso('Música atualizada')
        voltarApresentarTabela()
    } catch (erro) {
        console.error('Erro salvar nova musica', erro)
        alertarErro('Falha ao salvar')
    }
}

const salvarNovaMusica = async (musica) => {
    try {
        await ApiMusica.inserir(musica)
        alertarSucesso('Música salva')
        voltarApresentarTabela()
    } catch (erro) {
        console.error('Erro salvar nova musica', erro)
        alertarErro('Falha ao salvar')
    }

}

const mostrarPainelNovaMusica = () => {
    paginaHttp.musica = { codigo: null }
    mostrarPainelEsconderTabela()
    popularFormulario(paginaHttp.musica)
}

const mostrarPainelEsconderTabela = () => {
    paginaHttp.divFormulario.classList.remove('d-none')
    paginaHttp.divTblmusicas.classList.add('d-none')
}

const mostrarTabelaEsconderFormulario = () => {
    paginaHttp.divFormulario.classList.add('d-none')
    paginaHttp.divTblmusicas.classList.remove('d-none')
}

const carregarDadosMusicaEdicao = (musica) => {
    popularFormulario(musica)
    mostrarPainelEsconderTabela()
}

const carregarMusicaEdicao = async (codigoMusica) => {
    paginaHttp.musica = null
    try {
        paginaHttp.musica = await ApiMusica.pesquisarPeloCodigo(codigoMusica)
        carregarDadosMusicaEdicao(paginaHttp.musica)
    } catch (err) {
        console.error('Falha carrega musica pelo codigo', err)
        alertarErro('Falha carregar dados da música')
    }
}


// -------------------------------------
// Controlador tabela
// -------------------------------------

const voltarApresentarTabela = () => {
    paginaHttp.musica = null
    mostrarTabelaEsconderFormulario()
    carregarTodosTabela()
}


const editarRegistroTabela = (codigoRegistro) => {
    carregarMusicaEdicao(codigoRegistro)
}

const removerMusicaPeloCodigo = async (codigoMusica) => {

    try {
        const retorno = await ApiMusica.removerPeloCodigo(codigoMusica)
        alertarSucesso('Música removida!')
    } catch (err) {
        console.error('Falha ao remover a musica pelo código', err)
        alertarErro('Falha ao remover a música')
    } finally {
        carregarTodosTabela()
    }

}

const removerRegistroTabela = (codigoRegistro) => {
    // Deveria perguntar ao usuário?
    removerMusicaPeloCodigo(codigoRegistro)
}

const mapearLinhaTabela = (registro) => {
    return (
        '<tr><td>' +
        registro.nome +
        '</td><td>' +
        registro.artista +
        '</td><td>' +
        (registro.tempo || '-') +
        '</td><td>' +
        `<button type="button" class="btn btn-info" onclick="editarRegistroTabela('${registro.codigo}')"` +
        '><i class="bi bi-pencil-square"></i></button>' +
        `<button type="button" class="btn btn-danger" onclick="removerRegistroTabela('${registro.codigo}')"` +
        '><i class="bi bi-eraser"></i></button>' +
        '</td></tr>'
    )
}

const listarMusicasTabela = (listaMusicas) => {
    let conteudoTabela = ''

    if (!listaMusicas || !listaMusicas.length) {
        conteudoTabela = '<tr><td colspan="4"><i>Sem registros!</i></td></tr>'
    } else {
        let linhas = listaMusicas.map(mapearLinhaTabela)
        conteudoTabela = linhas.join('\n')
    }
    paginaHttp.tbodyTblMusicas.innerHTML = conteudoTabela
}


const carregarTodosTabela = async () => {
    let listaMusicas
    try {
        listaMusicas = await ApiMusica.pesquisarTodas()
    } catch (err) {
        console.error('Deu erro aqui meu amigo....', err)
        alertarErro(err.mensagem || ('' + err))
        listaMusicas = []
    }
    listarMusicasTabela(listaMusicas)
}

const gerenciarTabela = (paginaHttp) => {
    carregarTodosTabela(paginaHttp)
}

// -------------------------------------
// Controlador da página
// -------------------------------------

const carregarEventosPagina = () => {
    const bntNovaMusica = document.getElementById('btnnovo')
    bntNovaMusica.addEventListener('click', mostrarPainelNovaMusica)
    const btnCancelar = document.getElementById('btncancelar')
    btnCancelar.addEventListener('click', voltarApresentarTabela)
    const btnSalvar = document.getElementById('btnsalvar')
    btnSalvar.addEventListener('click', salvarRegistro)
}

const carregarElementosPagina = () => {
    paginaHttp.divAlertasSistema = document.getElementById('alertassistema'),
        paginaHttp.divTblmusicas = document.getElementById('divtblmusicas')
    paginaHttp.tblMusicas = document.getElementById('tblmusicas')
    paginaHttp.divFormulario = document.getElementById('divformulario')
    paginaHttp.txtNome = document.getElementById('txtnome')
    paginaHttp.txtArtista = document.getElementById('txtartista')
    paginaHttp.txtTempo = document.getElementById('txttempo')
    paginaHttp.tbodyTblMusicas = paginaHttp.tblMusicas.getElementsByTagName('tbody')[0]
    return paginaHttp
}

const iniciarControladorPagina = () => {
    console.debug('Carregando controlador da pagina')

    carregarElementosPagina()
    carregarEventosPagina()
    paginaHttp.divFormulario.classList.add('d-none')
    gerenciarTabela(paginaHttp)
}

iniciarControladorPagina()