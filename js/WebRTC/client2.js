// Client 2
const configuration = { iceServers: [{ urls: 'stun:stun.l.google.com:19302' }] };

// Create WebSocket for signaling server
const signalingServer = new WebSocket('ws://192.168.109.38:8765');

// Create RTCPeerConnection
const peerConnection = new RTCPeerConnection(configuration);

signalingServer.addEventListener('message', (event) => {
  const message = JSON.parse(event.data);

  if (message.offer) {
    peerConnection.setRemoteDescription(message.offer)
      .then(() => {
        return peerConnection.createAnswer();
      })
      .then((answer) => {
        return peerConnection.setLocalDescription(answer);
      })
      .then(() => {
        signalingServer.send(JSON.stringify({ answer: peerConnection.localDescription }));
      });
  } else if (message.answer) {
    peerConnection.setRemoteDescription(message.answer);
  } else if (message.iceCandidate) {
    peerConnection.addIceCandidate(message.iceCandidate);
  }
});

peerConnection.addEventListener('datachannel', (event) => {
  const dataChannel = event.channel;

  dataChannel.addEventListener('open', () => {
    console.log('Data channel is open');
  });

  dataChannel.addEventListener('message', (event) => {
    console.log('Received message:', event.data);
  });
});