import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-analytics.js";

const firebaseConfig = {
  apiKey: "AIzaSyCfbYG9VoydGiZmIwcycjDF6PbIewBWcwo",
  authDomain: "kocosi.firebaseapp.com",
  projectId: "kocosi",
  storageBucket: "kocosi.appspot.com",
  messagingSenderId: "904913803495",
  appId: "1:904913803495:web:bcfe710ac7fc5b9eecea42",
  measurementId: "G-PJ2MDJBSDV"
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
import {getStorage, ref as sRef, uploadBytesResumable, getDownloadURL} from "https://www.gstatic.com/firebasejs/10.8.1/firebase-storage.js"

var files = [];
var reader = new FileReader();

var namebox = document.getElementById('namebox');
var extlab = document.getElementById('extlab');
var myimg = document.getElementById('myimg');
var proglab = document.getElementById('upprogress');
var SelBtn = document.getElementById('selbtn');
var UpBtn = document.getElementById('upbtn');
var DownBtn = document.getElementById('downbtn');

var input = document.createElement('input');
input.type = 'file';

input.onchange = e => {
files = e.target.files;
var extension = GetFileExt(files[0]);
var name = GetFileName(files[0]);
namebox.value = name;
extlab.innerHTML = extension; 
reader.readAsDataURL(files[0]);
};


reader.onload = function() {
myimg.src = reader.result;
};


SelBtn.onclick = function() {
    input.click();
};

function GetFileExt(file){
    var temp = file.name.split('.');
    var ext = temp.slice((temp.length - 1), (temp.length));
    return '.' + ext[0];
}

function GetFileName(file){
    var temp = file.name.split('.');
    var fname = temp.slice(0, -1).join('.');
    return fname;
}

async function UploadProcess(name) {
var ImgToUpload = files[0];
var ImgName = name + extlab.innerHTML; 
const metaData = {
    contentType: ImgToUpload.type
}

const storage = getStorage();
const storageRef = sRef(storage, "Images/" + ImgName);
try {
    const snapshot = await uploadBytesResumable(storageRef, ImgToUpload, metaData);
    var downloadURL = await getDownloadURL(snapshot.ref);
    console.log("Image uploaded successfully. Download URL:", downloadURL);
} catch (error) {
    console.error("Error uploading image:", error);
    alert("Error: Image not uploaded!");
}
}

async function GetImageFromFirestore1(name){
const storage = getStorage();
const storageRef = sRef(storage, "Images/" + name);

try {
    const downloadURL = await getDownloadURL(storageRef);
    //tuk slagame samata snimka
    myimg.src = downloadURL;
    console.log("Image retrieved successfully:", downloadURL);
} catch (error) {
    console.error("Error retrieving image:", error);
    alert("Error: Image not found!");
}
}