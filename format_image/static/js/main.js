document.getElementById('fileInput').addEventListener('change', function(event) {
        var file = event.target.files[0];
        if (file) {
            var fileName = file.name;
            var fileNameWithoutExtension = fileName.substring(0, fileName.lastIndexOf('.'));
            document.getElementById('output').value = fileNameWithoutExtension;
        }
    });

window.onload = function() {
var img = document.getElementById('image');
if (img.naturalWidth > img.naturalHeight) {
  img.style.width = '85%';
  img.style.height = 'auto';
} else {
  img.style.width = 'auto';
  img.style.height = '85%';
}
};



