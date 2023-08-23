// Client 1
const configuration = { iceServers: [{ urls: 'stun:stun.l.google.com:19302' }] };

// Create WebSocket for signaling server
const signalingServer = new WebSocket('ws://192.168.109.38:8765');

// Create RTCPeerConnection and data channel
const peerConnection = new RTCPeerConnection(configuration);
const dataChannel = peerConnection.createDataChannel('dataChannel');

dataChannel.addEventListener('open', () => {
  console.log('Data channel is open');
});

dataChannel.addEventListener('message', (event) => {
  console.log('Received message:', event.data);
});

peerConnection.addEventListener('icecandidate', (event) => {
  if (event.candidate) {
    signalingServer.send(JSON.stringify({ iceCandidate: event.candidate }));
  }
});

peerConnection.createOffer()
  .then((offer) => {
    return peerConnection.setLocalDescription(offer);
  })
  .then(() => {
    signalingServer.send(JSON.stringify({ offer: peerConnection.localDescription }));
  });