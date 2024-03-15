import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
    import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-analytics.js";
    require('dotenv').config();

    const firebaseConfig = {
      apiKey: process.env.FIREBASE_API_KEY,
      authDomain: process.env.FIREBASE_AUTH_DOMAIN,
      projectId: process.env.FIREBASE_PROJECT_ID,
      storageBucket: process.env.FIREBASE_STORAGE_BUCKET,
      messagingSenderId: process.env.FIREBASE_MESSAGING_SENDER_ID,
      appId: process.env.FIREBASE_APP_ID,
      measurementId: process.env.FIREBASE_MEASUREMENT_ID
    };
  
    const app = initializeApp(firebaseConfig);
    const analytics = getAnalytics(app);
    import {getStorage, ref as sRef, uploadBytesResumable, getDownloadURL} from "https://www.gstatic.com/firebasejs/10.8.1/firebase-storage.js"

    // var files = [];
    // var reader = new FileReader();

    // var namebox = document.getElementById('namebox');
    // var extlab = document.getElementById('extlab');
    // var myimg = document.getElementById('myimg');
    // var proglab = document.getElementById('upprogress');
    // var SelBtn = document.getElementById('selbtn');
    // var UpBtn = document.getElementById('upbtn');
    // var DownBtn = document.getElementById('downbtn');

    // var input = document.createElement('input');
    // input.type = 'file';

    // input.onchange = e => {
    // files = e.target.files;
    // var extension = GetFileExt(files[0]);
    // var name = GetFileName(files[0]);
    // namebox.value = name;
    // extlab.innerHTML = extension; 
    // reader.readAsDataURL(files[0]);
    // };


    // reader.onload = function() {
    // myimg.src = reader.result;
    // };


    // SelBtn.onclick = function() {
    //     input.click();
    // };

    // function GetFileExt(file){
    //     var temp = file.name.split('.');
    //     var ext = temp.slice((temp.length - 1), (temp.length));
    //     return '.' + ext[0];
    // }

    // function GetFileName(file){
    //     var temp = file.name.split('.');
    //     var fname = temp.slice(0, -1).join('.');
    //     return fname;
    // }

    // async function UploadProcess() {
    // var ImgToUpload = files[0];
    // var ImgName = namebox.value + extlab.innerHTML; 
    // const metaData = {
    //     contentType: ImgToUpload.type
    // }

    // const storage = getStorage();
    // const storageRef = sRef(storage, "Images/" + ImgName);
    // try {
    //     const snapshot = await uploadBytesResumable(storageRef, ImgToUpload, metaData);
    //     var downloadURL = await getDownloadURL(snapshot.ref);
    //     console.log("Image uploaded successfully. Download URL:", downloadURL);
    // } catch (error) {
    //     console.error("Error uploading image:", error);
    //     alert("Error: Image not uploaded!");
    // }
    // }

    async function GetImageFromFirestore1(name){
    const storage = getStorage();
    const storageRef = sRef(storage, "Images/" + name);
    
    try {
        const downloadURL = await getDownloadURL(storageRef);
        return downloadURL;
        console.log("Image retrieved successfully:", downloadURL);
    } catch (error) {
        console.error("Error retrieving image:", error);
        alert("Error: Image not found!");
    }
}
