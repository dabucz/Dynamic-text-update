<template>
  <div>
    <div>
      <div class="nuke-overlay">
        <div class="nuke-overlay__slide-name"> Nuke win streak </div>
        <div class="nuke-overlay__inner" style="background-color: rgb(0, 0, 0); border-color: rgb(136, 136, 136); border-radius: 45px; border-width: 5px; color: rgb(255, 255, 255);"><!---->
          <div class="nuke-overlay-content"><div class="nuke-overlay-content__slide">
            {{ Texttt }} / 5 </div>
        </div></div>
        <img src="https://overlay.wzhub.gg/images/achievements/nukes2.svg" class="nuke-overlay__icon" style="animation-name: rotation; animation-iteration-count: infinite; animation-timing-function: linear; animation-duration: 2s;"></div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      Texttt: "0",
    }
  },
  mounted() {
    const socket = new WebSocket('ws://localhost:8000');
    socket.addEventListener('message', (event) => {
      this.Texttt = event.data;
    });
  }
}
</script>
