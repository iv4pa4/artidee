const usernameInput = document.getElementById('username');
const addButton = document.getElementById('add');

function addFriend(username) {
	const url = 'https://quant.pythonanywhere.com/add_friend';
	console.log(localStorage.getItem('userID'))
	console.log(username)

	const data = {
		user_id: localStorage.getItem('userID'),
		name: username
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
		window.location.href = '../friends/friends.html';
	})
	.catch((error) => {
  		console.error('Error:', error);
	});
}

addButton.addEventListener('click', function() {
	const usernameText = usernameInput.value;
	addFriend(usernameText);
});

