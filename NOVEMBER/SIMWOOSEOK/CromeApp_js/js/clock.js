const clock = document.querySelector('h2#clock')

function getClock() {
  const date = new Date()
  const hours = String(date.getHours()).padStart(2,'0')
  const minutes = String(date.getMinutes()).padStart(2,'0')
  const second = String(date.getSeconds()).padStart(2,'0')
  clock.innerText = `${hours}:${minutes}:${second}`
}

getClock()
setInterval(getClock, 1000)
// setInterval() 를 쓰지 않으면 처음 시간만 출력되고 갱신되지않는다