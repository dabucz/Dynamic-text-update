<template>
  <div>
    <h1>My Vue.js App</h1>
    <div>
      <p>{{ Nuke }}/5</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      Nuke: null
    }
  },
  mounted() {
    const socket = new WebSocket('ws://localhost:8000');
    socket.addEventListener('message', (event) => {
      this.Nuke = event.data;
    });
  }
}
</script>
