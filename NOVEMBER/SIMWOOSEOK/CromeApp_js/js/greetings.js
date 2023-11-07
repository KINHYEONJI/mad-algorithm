const loginInput = document.querySelector('#login-form input')
const loginForm = document.querySelector('#login-form')
const greeting = document.querySelector('#greeting')
const HIDDEN_CLASSNAME = 'hidden'  // 숨기기
const USERNAME_KEY = 'username'    // 사용자이름 넣어두기


function onLoginSubmit(event) {
  event.preventDefault() // 3) 새로고침 방지, submit 제출 x
  loginForm.classList.add('hidden') // 4) form을 숨겨줌
  const username = loginInput.value // 5) inputForm의 값을 username으로 지칭
  // function안에서 input값을 받는 이유?
  // username을 함수 밖에 선언하게 되면 submit 하기 전에 input에 있는 value가 username에 저장
  localStorage.setItem(USERNAME_KEY, username);  // 6) 로컬저장소에 username을 저장
  paintGreetings(username);
}

function paintGreetings(username) {
  greeting.innerText = `Hello ${username}`;
  greeting.classList.remove(HIDDEN_CLASSNAME);
}

loginForm.addEventListener("submit", onLoginSubmit);
const savedUsername = localStorage.getItem(USERNAME_KEY);
// 1) 로컬스토리지에 정보가 있는지 확인

if (savedUsername === null) {
  loginForm.classList.remove(HIDDEN_CLASSNAME);
  loginForm.addEventListener("submit", onLoginSubmit);
  // 2) 만약 정보가 비어있다면 form에 eventlistener를 더하고 submit을 기다림

} else {
  paintGreetings(savedUsername);

}