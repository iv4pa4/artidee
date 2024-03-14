const images = getImages();

function loadImages() {
    const gallery = document.getElementById('gallery');

    images.forEach((src) => {
        const box = document.createElement('div');
        box.className = 'box';

        const img = document.createElement('img');
        img.src = src;

        img.onclick = function() {
            const modal = document.getElementById('imagePopup');
            const modalImg = document.getElementById('popupImg');
            modal.style.display = "block";
            modalImg.src = this.src;
        };

        box.appendChild(img);
        gallery.appendChild(box);
    });

    const modal = document.getElementById('imagePopup');

    const span = document.getElementsByClassName("close")[0];

    span.onclick = function() { 
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}

function getImages() {
    const res = [ //call backend here :)
        'image/icon-1.png',
        'image/icon-2.png',
        'image/icon-3.png',
        'image/icon-4.png',
        'image/icon-5.png',
        'image/icon-6.png',
    ];
    
    return res;
}

loadImages();
