const friends = getFriends();

const addButton = document.getElementById('add');

add.addEventListener('click', () => {
    window.location.href = '../add%20friend/add.html';
})

function loadFriends() {
    const friendsList = getFriends();
    const friendsContainer = document.getElementById('friends'); 

    friendsList.forEach((friend) => { 
        const { id, name } = friend; // Correctly destructuring the object here

        const box = document.createElement('div');
        box.className = 'box';

        const descElement = document.createElement('p');
        descElement.textContent = name;
        descElement.className = 'image-description';
    
        descElement.onclick = function() {
            localStorage.setItem('friendName', name);
            window.location.href = '../gallery/gallery.html';
        }

        box.appendChild(descElement);
        friendsContainer.appendChild(box);
    });

}


function getFriends() {
    const res = [ //call backend here :)
        { id: 'id 1', name: 'Friend 1' },
        { id: 'id 2', name: 'Friend 2' },
        { id: 'id 3', name: 'Friend 3' },
        { id: 'id 4', name: 'Friend 4' },
        { id: 'id 5', name: 'Friend 5' },
        { id: 'id 6', name: 'Friend 6' },
    ];
    
    return res;
}

loadFriends();
