const usernameInput = document.getElementById('username');
const addButton = document.getElementById('add');

function addFriend(username) {//TODO
    const url = 'https://quant.pythonanywhere.com/???';

	const data = {
		userId: localStorage.getItem('userID'),
		friendName: usernameInput
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

