/**
 * Retorna a data e hora atuais para a criação da mensagem.
 */
function getCurrentTimestamp() {
    return new Date();
}

/**
 * Renderiza uma mensagem na tela do chat com base nos argumentos fornecidos.
 * Isso é chamado a partir das funções `showUserMessage` e `showBotMessage`.
 */
function renderMessageToScreen(args) {
    let displayDate = (args.time || getCurrentTimestamp()).toLocaleString('pt-BR', {
        month: 'short',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
    });
    let messagesContainer = $('.messages');

    let message = $(`
    <li class="message ${args.message_side}">
        <div class="avatar"></div>
        <div class="text_wrapper">
            <div class="text">${args.text}</div>
            <div class="timestamp">${displayDate}</div>
        </div>
    </li>
    `);

    messagesContainer.append(message);

    setTimeout(function () {
        message.addClass('appeared');
    }, 0);
    messagesContainer.animate({ scrollTop: messagesContainer.prop('scrollHeight') }, 300);
}

/* Envia uma mensagem quando a tecla 'Enter' é pressionada.
 */
$(document).ready(function() {
    $('#msg_input').keydown(function(e) {
        // Verifica se a tecla 'Enter' foi pressionada
        if (e.key === 'Enter') {
            // Impede o comportamento padrão da tecla 'Enter'
            e.preventDefault();
            // Aciona o evento de clique do botão de enviar
            $('#send_button').click();
        }
    });
});

/**
 * Exibe a mensagem do usuário na tela do chat. Esta é a mensagem do lado direito.
 */
function showUserMessage(message, datetime) {
    renderMessageToScreen({
        text: message,
        time: datetime,
        message_side: 'right',
    });
}

/**
 * Exibe a mensagem do chatbot na tela do chat. Esta é a mensagem do lado esquerdo.
 */
function showBotMessage(message, datetime) {
    renderMessageToScreen({
        text: message,
        time: datetime,
        message_side: 'left',
    });
}

/**
 * Obtém a entrada do usuário e mostra na tela ao clicar no botão.
 */
$('#send_button').on('click', function (e) {
    // Obtém e mostra a mensagem do usuário
    let userMessage = $('#msg_input').val();
    showUserMessage(userMessage);
    $('#msg_input').val('');

    // Mostra a mensagem do bot
    setTimeout(function () {
        showBotMessage(randomResposta());
    }, 300);
});

/**
 * Retorna uma resposta aleatória do bot.
 */
function randomResposta() {
    // Escolhe aleatoriamente uma resposta do array de respostas do bot em português
    return respostasBot[Math.floor(Math.random() * respostasBot.length)];
}

// Array de respostas do bot em português
const respostasBot = [
    "Olá! Como posso ajudar?",
    "Qual é a sua dúvida?",
    "Estou aqui para te ajudar!",
    "Como posso ser útil hoje?",
    "Pergunte-me qualquer coisa!",
    "Espero poder ser útil para você!",
    "Vamos lá! Estou pronto para responder suas perguntas."
];

<<<<<<< HEAD
$(window).on('load', function () {
    for (let i = 0; i < 4; i++) {
        showBotMessage('Olá! Como posso ajudar?');
    }
});


 setTimeout(function () {
        $('.messages .message').addClass('side-by-side');
    }, messages.length * 1000);
 
=======
/**
 * Set initial bot message to the screen for the user.
 */
$(window).on('load', function () {
    showBotMessage('Olá! Como posso ajudar?');
});
>>>>>>> 3ae86399bcb30d7da5730a423cc6a65f8a2f90ea
