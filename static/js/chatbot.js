window.addEventListener('load', function() {
  var script = document.createElement('script');
  script.src = 'https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1';
  document.head.appendChild(script);

  var dfMessenger = document.createElement('df-messenger');
  dfMessenger.setAttribute('chat-title', 'parapharmacy-bot');
  dfMessenger.setAttribute('agent-id', '5a38c805-f56b-4e38-bee1-26d2bd9c62b5'); // Replace this with your actual agent ID
  dfMessenger.setAttribute('language-code', 'en');
  document.body.appendChild(dfMessenger);
});
