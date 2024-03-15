const friends = getFriends();

const addButton = document.getElementById('add');

add.addEventListener('click', () => {
    window.location.href = '../add%20friend/add.html';
})

function loadFriends() {
    const friendsList = getFriends();
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



function getFriends() {
    const res = [ //call backend here :)
        { id: 'y0VZI93ePBbtsVIW5SF9lIA3rJA2', name: 'Friend 1' },
        { id: 'y0VZI93ePBbtsVIW5SF9lIA3rJA2', name: 'Friend 2' },
        { id: 'y0VZI93ePBbtsVIW5SF9lIA3rJA2', name: 'Friend 3' },
        { id: 'y0VZI93ePBbtsVIW5SF9lIA3rJA2', name: 'Friend 4' },
        { id: 'y0VZI93ePBbtsVIW5SF9lIA3rJA2', name: 'Friend 5' },
        { id: 'y0VZI93ePBbtsVIW5SF9lIA3rJA2', name: 'Friend 6' },
    ];
    
    return res;
}

loadFriends();
