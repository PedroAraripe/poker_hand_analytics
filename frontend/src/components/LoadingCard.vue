<template>
  <div class="wrapper-loading-card">
    <div class="card-container">
      <div class="card">
        <!-- Ás de Espadas -->
        <div class="face front-ace">
          <div class="corner">A<br />♠</div>
          <div class="suit">♠</div>
          <div class="corner" style="align-self: flex-end; transform: rotate(180deg)">A<br />♠</div>
        </div>
        <!-- Verso -->
        <div class="face back"></div>
      </div>
    </div>

    <!-- <div style="margin-top: 1rem">Carregando estatísticas...</div> -->
  </div>
</template>

<style lang="scss" scoped>
.wrapper-loading-card {
  position: absolute;
  left: 0;
  top: 0;
  z-index: 100;
  background: #ffffff;

  height: 100vh;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.card-container {
  &,
  & * {
    font-weight: bold;
  }
}

body {
  background: #121212;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  perspective: 800px;
  margin: 0;
}

.card-container {
  width: 80px;
  height: 120px;
  animation: spin 2s linear infinite;
  transform-style: preserve-3d;
}

.card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
}

.face {
  position: absolute;
  width: 100%;
  height: 100%;
  border-radius: 8px;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: Arial, sans-serif;
  font-weight: bold;
  backface-visibility: hidden;
  border: 2px solid #000;
}

.front-ace {
  background: white;
  flex-direction: column;
  padding: 6px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  color: red;
  animation: none; /* Remove the animation from the front face */
}

.front-ace {
  color: black;
}

.back {
  transform: rotateY(180deg);
  animation: alternateBack 4s linear infinite;
  background-size: 20px 20px;
}

@keyframes alternateBack {
  0%,
  50% {
    background-color: #004080;
    background-image: url("data:image/svg+xml,%3Csvg width='20' height='20' viewBox='0 0 10 10' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%23ffffff' fill-opacity='0.2'%3E%3Ccircle cx='1' cy='1' r='1'/%3E%3Ccircle cx='6' cy='1' r='1'/%3E%3Ccircle cx='1' cy='6' r='1'/%3E%3Ccircle cx='6' cy='6' r='1'/%3E%3C/g%3E%3C/svg%3E");
  }
  50.01%,
  100% {
    background-color: #800000;
    background-image: url("data:image/svg+xml,%3Csvg width='20' height='20' viewBox='0 0 10 10' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%23ffffff' fill-opacity='0.2'%3E%3Ccircle cx='1' cy='1' r='1'/%3E%3Ccircle cx='6' cy='1' r='1'/%3E%3Ccircle cx='1' cy='6' r='1'/%3E%3Ccircle cx='6' cy='6' r='1'/%3E%3C/g%3E%3C/svg%3E");
  }
}

/* Controla a troca de faces enquanto o verso está visível */
.card-container {
  animation: spin 2s linear infinite;
}

.card-container:hover .front-ace {
  opacity: 1;
}

.corner {
  font-size: 14px;
  line-height: 1;
  align-self: flex-start;
}

.suit {
  font-size: 28px;
  margin-top: 16px;
}

@keyframes spin {
  0% {
    transform: rotateY(0deg);
  }
  50% {
    transform: rotateY(180deg);
  }
  100% {
    transform: rotateY(360deg);
  }
}
</style>
