<template>
{{ Texttt }}
</template>

<script>
export default {
  data() {
    return {
      Texttt: "0",
    }
  },
  mounted() {
    const socket = new WebSocket('ws://192.168.1.19:8000'); // your websocket ip here
    socket.addEventListener('message', (event) => {
      this.Texttt = event.data;
    });
  }
}
</script>
