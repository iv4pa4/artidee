const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const doSignUpButton = document.getElementById('signUpButton');
const doLoginButton = document.getElementById('loginButton');
const container = document.getElementById('container');

const signupName = document.getElementById('signupName')

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

doSignUpButton.addEventListener('click', () => {
	const url = 'https://quant.pythonanywhere.com/signup';

	const data = {
		name: signupName.value,
		email: document.getElementById('signupEmail').value,
		password: document.getElementById('signupPassword').value,
		level: parseInt(document.querySelector('input[name="difficultyLevel"]:checked').value)
	};

	fetch(url, {
		method: 'POST', 
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(data),
	})
	.then(response => response.json())
	.then(data => {
  		console.log('Success:', data);
  		console.log('Message:', data.message);
		localStorage.setItem('userID', data.message);
		window.location.href = '../main%20page/main.html';
	})
	.catch((error) => {
  		console.error('Error:', error);
	});
});

doLoginButton.addEventListener('click', () => {
	const url = 'https://quant.pythonanywhere.com/login';

	const data = {
		email: document.getElementById('loginEmail').value,
		password: document.getElementById('loginPassword').value
	};
	
	fetch(url, {
		method: 'POST', 
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(data),
	})
	.then(response => {
		if (!response.ok) {
			throw new Error('Network response was not ok');
		}
		return response.json();
	})
	.then(data => {
  		console.log('Success:', data);
  		console.log('Message:', data.message);
		localStorage.setItem('userID', data.message);
		window.location.href = '../main%20page/main.html';
	})
	.catch((error) => {
  		console.error('Error:', error);
	});
});
