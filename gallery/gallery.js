const images = getImages();

function loadImages() {
    const gallery = document.getElementById('gallery');

    images.forEach(({src, description}) => {
        const box = document.createElement('div');
        box.className = 'box';

        const descElement = document.createElement('p');
        descElement.textContent = description;
        descElement.className = 'image-description';

        const img = document.createElement('img');
        img.src = src;

        img.onclick = function() {
        document.getElementById('imagePopup').style.display = "block";
        document.getElementById('popupImg').src = this.src;
        document.getElementById('caption').innerText = description;
        document.body.classList.add('no-scroll');
        };

        window.onclick = function(event) {
        if (event.target == modal) {
                modal.style.display = "none";
                document.body.classList.remove('no-scroll');
            }
        }

        box.appendChild(descElement);
        box.appendChild(img);
        gallery.appendChild(box);
    });

    const modal = document.getElementById('imagePopup');

}

function getImages() {
    const res = [ //call backend here :)
        { src: 'image/icon-1.png', description: 'Description for Image 1' },
        { src: 'image/icon-2.png', description: 'Description for Image 2' },
        { src: 'image/icon-3.png', description: 'Description for Image 3' },
        { src: 'image/icon-4.png', description: 'Description for Image 4' },
        { src: 'image/icon-5.png', description: 'Description for Image 5' },
        { src: 'image/icon-6.png', description: 'Description for Image 6' },
    ];
    
    return res;
}

loadImages();
