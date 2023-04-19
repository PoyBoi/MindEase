const inputMessage = document.getElementById('userBox');
const sendButton = document.getElementById('sendButton');
const chatMessages = document.querySelector('.box');

sendButton.addEventListener('click', sendMessage);
inputMessage.addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
    sendMessage();
  }
});

function sendMessage() 
{
  const message = inputMessage.value;
  if (message) 
  {
    addMessageToChat('user', message);
    inputMessage.value = '';

    // Add your own custom response messages here
    if (message === 'Hi' || message === 'Hello' || message === 'Hey' || message === 'Hi there' || message === 'Hello there' || message === 'Hey there' || message === 'Hi there!' || message === 'Hello there!' || message === 'Hey there!' || message === 'hi' || message === 'hello' || message === 'hey' || message === 'hi there' || message === 'hello there' || message === 'hey there' || message === 'hi there!' || message === 'hello there!' || message === 'hey there!') {
        setTimeout(() => {
        const botMessage = 'Hello! How are you?';
        addMessageToChat('bot', botMessage);
        }, 1000);
    }

    else if (message === 'i am okay' || message === 'not feeling good' || message === 'not great' || message === 'not good' || message === 'not okay' || message === 'not well' || message === 'not good.' || message === 'not okay.' || message === 'not well.' || message === 'not great.' || message === 'I am okay' || message === 'Not feeling good' || message === 'Not great' || message === 'Not good' || message === 'Not okay' || message === 'Not well' || message === 'Not good.' || message === 'Not okay.' || message === 'Not well.' || message === 'Not great.' || message === 'I am okay.' || message === 'Not feeling good.' || message === 'Not great.' || message === 'Not good.' || message === 'Not okay.' || message === 'Not well.' || message === 'I am okay!' || message === 'Not feeling good!' || message === 'Not great!' || message === 'Not good!' || message === 'Not okay!' || message === 'Not well!' || message === 'I am okay!' || message === 'Not feeling good!' || message === 'Not great!' || message === 'Not good!' || message === 'Not okay!' || message === 'Not well!' || message === 'I am okay!' || message === 'Not feeling good!' || message === 'Not great!' || message === 'Not good!' || message === 'Not okay!' || message === 'Not well!' || message === 'I am okay!' || message === 'Not feeling good!' || message === 'Not great!' || message === 'Not good!' || message === 'Not okay!' || message === 'Not well!' || message === 'I am okay!' || message === 'Not feeling good!' || message === 'Not great!' || message === 'Not good!' || message === 'Not okay!' || message === 'Not well!') {
        setTimeout(() => {
        const botMessage = 'Why? What happened? Would you like to talk about it?';
        addMessageToChat('bot', botMessage);
        }, 1000);
    }

    // else if (message === 'How are you?' || message === 'how are you?' || message === 'How are you doing?' || message === 'how are you doing?' || message === 'How are you doing today?' || message === 'how are you doing today?' || message === 'How are you doing today' || message === 'how are you doing today' || message === 'How are you doing today?' || message === 'how are you doing today?') {
    //     setTimeout(() => {
    //     const botMessage = 'I am doing well, thank you for asking. How are you feeling today?';
    //     addMessageToChat('bot', botMessage);
    //     }, 1000);
    // }

    else if (message === 'I am not feeling good' || message === 'Today was not good' || message === 'i am not feeling good' || message === 'today was not good' || message === 'I am not feeling good.' || message === 'Today was not good.' || message === 'i am not feeling good.' || message === 'today was not good.' || message === 'i am not okay' || message === 'I am not okay') {
        setTimeout(() => {
            const botMessage = 'Why? What happened? Would you like to talk about it?';
            addMessageToChat('bot', botMessage);
        }, 1900);
    }

    else if (message === 'Yes' || message === 'yes' || message === 'Yes.' || message === 'yes.' || message === 'Yes!' || message === 'yes!') {
        setTimeout(() => {
            const botMessage = 'Tell me about it. I am here to listen.';
            addMessageToChat('bot', botMessage);
        }, 1900);
    }

    else if (message === 'No' || message === 'no' || message === 'No.' || message === 'no.' || message === 'No!' || message === 'no!') {
        setTimeout(() => {
            const botMessage = 'You can talk to me about anything. I will help you.';
            addMessageToChat('bot', botMessage);
        }, 1900);
    }

    else if (message === 'okay' || message === 'Okay' || message === 'okay.' || message === 'Okay.' || message === 'okay!' || message === 'Okay!') {
        setTimeout(() => {
            const botMessage = 'Great!, tell me about your day.';
            addMessageToChat('bot', botMessage);
        }, 1500);
    }

    else if (message === 'nothing much, today was not as great' || message === 'nothing much, today was not as great.' || message === 'Nothing much, today was not as great!'){
        setTimeout(() => {
            const botMessage = 'Why?';
            addMessageToChat('bot', botMessage);
        }, 1000);
    }

    else if (message === 'i dont know, i just feel sad and unmotivated all the time' || message === 'i dont know, i am feeling a bit down lately') {
        setTimeout(() => {
            const botMessage = 'That sounds really tough. Have you talked to anyone about it, like a friend or family member?';
            addMessageToChat('bot', botMessage);
        }, 2900);
    }

    else if (message === 'no i dont want to burden anyone with my problems' || message === 'no i dont want to share it with anyone'){
        setTimeout(() => {
            const botMessage = 'It is important to remember that talking to someone about your feelings is not a burden.';
            addMessageToChat('bot', botMessage);
        }, 2500);

        setTimeout(() => {
            const botMessage = 'In fact, it can often help to share your thoughts with someone you trust';
            addMessageToChat('bot', botMessage);
        }, 4400);
    }

    else if (message === 'i dont know if that would help' || message === 'it might not help me'){
        setTimeout(() => {
            const botMessage = 'It is definitely worth a try. Therapy can be a really effective way to manage symptoms of depression and improve your overall well-being';
            addMessageToChat('bot', botMessage);
        }, 3800);
    }

    else if (message === 'i dont really have friends nearby, i am just bad at making friends'){
        setTimeout(() => {
            const botMessage = 'It can be tough, but remember that everyone feels awkward sometimes';
            addMessageToChat('bot', botMessage);
        }, 2500);

        setTimeout(() => {
            const botMessage = 'And remember that making friends takes time, it is okay if it does not happen overnight';
            addMessageToChat('bot', botMessage);
        }, 4200);
    }

    else if (message === 'i will try, but i just feel so hopeless'){
        setTimeout(() => {
            const botMessage = 'I know it can feel that way sometimes, but it is important to hold on to hope.';
            addMessageToChat('bot', botMessage);
        }, 2900);

        setTimeout(() => {
            const botMessage = 'By far, i have analysed that you some symptoms of a mild depression.';
            addMessageToChat('bot', botMessage);
        }, 4000);
        
        setTimeout(() => {
            const botMessage = 'But it is okay, you can get through this. It is a treatable condition, and with the right support, many people are able to make a full recovery';
            addMessageToChat('bot', botMessage);
        }, 6090);

        setTimeout(() => {
            const botMessage = 'I will help you through this, you can talk to me about anything. And i will recommend you some experts who can help you if you want';
            addMessageToChat('bot', botMessage);
        }, 7800);
    }

    else if (message === 'i am feeling a bit better now, thank you for listening'){
        setTimeout(() => {
            const botMessage = 'I am glad to hear that. I am here to listen to you anytime you need me.';
            addMessageToChat('bot', botMessage);
        }, 2800);

        setTimeout(() => {
            const botMessage = ' In the meantime, there are some other things you can try to help boost your mood, like getting regular exercise, practicing mindfulness, and connecting with others.';
            addMessageToChat('bot', botMessage);
        }, 4600);
        
    }

    else if (message === 'thank you, i will try those things'){
        setTimeout(() => {
            const botMessage = 'Wonderful!';
            addMessageToChat('bot', botMessage);
        }, 1800);
    }

    else if (message === 'bye'){
        setTimeout(() => {
            const botMessage = 'Bye, take care.';
            addMessageToChat('bot', botMessage);
        }, 2000);
    }

    else {
      setTimeout(() => {
        const botMessage = 'I am sorry, I did not understand.';
        addMessageToChat('bot', botMessage);
        }, 1000);
    }
  }
}

function addMessageToChat(sender, message) 
{
  const messageWrapper = document.createElement('div');
  messageWrapper.classList.add('chat-message');

  const messageContent = document.createElement('div');
  messageContent.classList.add(`${sender}-message`);
  messageContent.textContent = message;

  messageWrapper.appendChild(messageContent);
  chatMessages.appendChild(messageWrapper);

  chatMessages.scrollTop = chatMessages.scrollHeight;
}
