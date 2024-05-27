document.getElementById('fileInput').addEventListener('change', function(event) {
        var file = event.target.files[0];
        if (file) {
            var fileName = file.name;
            var fileNameWithoutExtension = fileName.substring(0, fileName.lastIndexOf('.'));
            document.getElementById('output').value = fileNameWithoutExtension;
        }
    });