const addButton = document.getElementById('add');

add.addEventListener('click', () => {
    window.location.href = '../add%20friend/add.html';
})

function loadFriends(friendsList) {
    const friendsContainer = document.getElementById('friends');

    friendsList.forEach((friend) => {
        const { id, name } = friend;

        const friendContainer = document.createElement('div');
        friendContainer.className = 'friend-container';

        const box = document.createElement('div');
        box.className = 'box';
        const descElement = document.createElement('p');
        descElement.textContent = name;
        descElement.className = 'image-description';
        box.appendChild(descElement);

        const buttonsContainer = document.createElement('div');
        buttonsContainer.className = 'buttons-container';

        const multiplePicturesButton = document.createElement('button');
        multiplePicturesButton.className = 'action-button multiple-pictures';
        multiplePicturesButton.onclick = () => console.log('Multiple Pictures Clicked');
        const multiplePicturesIcon = document.createElement('img');
        multiplePicturesIcon.src = 'multiple_pictures_icon.svg';
        multiplePicturesButton.appendChild(multiplePicturesIcon);

        const unfriendButton = document.createElement('button');
        unfriendButton.className = 'action-button unfriend';
        unfriendButton.onclick = () => console.log('Unfriend Clicked');
        const unfriendIcon = document.createElement('img');
        unfriendIcon.src = 'unfriend_icon.svg';
        unfriendButton.appendChild(unfriendIcon);

        buttonsContainer.appendChild(multiplePicturesButton);
        buttonsContainer.appendChild(unfriendButton);

        friendContainer.appendChild(box);
        friendContainer.appendChild(buttonsContainer);

        friendsContainer.appendChild(friendContainer);
    });
}



function getFriends(ids, names) {

    const res = ids.map((id, index) => {
        return { id: id, name: names[index] };
    });
    
    return res;
}

function loadMyFriends() {
    const userId = localStorage.getItem('userId');
    const url = new URL('https://quant.pythonanywhere.com/friends');
    url.searchParams.append('user_id', localStorage.getItem('userID')); // Append user_id as a query parameter

	const data = {
		user_id: localStorage.getItem('userID')
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
  		var friends = getFriends(data.friends, data.names)
                loadFriends(friends);
	})
	.catch((error) => {
  		console.error('Error:', error);
	});
}

loadMyFriends() 


