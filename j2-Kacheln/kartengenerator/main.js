function insertExample(){
  document.getElementById('input-area').value = "2\n2\n\n1 0   * * \n0 1   * * \n\n* *   1 0 \n* *   1 1 \n";
}

function deleteArea(){
  document.getElementById('input-area').value = "";
}

function downloadSVG(filename, id, text) {
  var element = document.getElementById(id);
  element.setAttribute('href', 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', filename);
  element.setAttribute('style', '');
}

function displaySVG(text) {
  var element = document.getElementById('svg');
  element.innerHTML = text;
}

function downloadPNG(filename, id, text) {
  var can = document.getElementById('canvas');
  var ctx = can.getContext('2d');
  var img = new Image();
  img.onload = function() {
    ctx.drawImage(img, 0, 0);
    var dataurl = can.toDataURL("image/png");

    var element = document.getElementById(id);
    element.setAttribute('href', dataurl);
    element.setAttribute('download', filename);
    element.setAttribute('style', '');
  };
  img.src = "data:image/svg+xml;base64," + btoa(text);
}

document.getElementById('input-form').addEventListener('submit', function(e) {
  var input = document.getElementById('input-area').value;

  var lines = input.split('\n');

  var length = parseInt(lines[0]);
  var width = parseInt(lines[1]);

  var can = document.getElementById('canvas');
  can.height = length*128;
  can.width = width*128;

  var factor = 6;
   
  var resultSVGwhite = '<svg height="' + length*128 + '" width="' + width*128 + '" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n';
  var resultSVGgray  = '<svg height="' + length*128 + '" width="' + width*128 + '" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n';

  for (var x = 0; x < width; ++x) {
    for (var y = 0; y < length; ++y) {
      var topRow = lines[3 * y + 3];
      var bottomRow = lines[3 * y + 4];

      if (topRow[factor * x] == '*' || topRow[factor * x + 2] == '*' || bottomRow[factor * x] == '*' || bottomRow[factor * x + 2] == '*') {
        var posx = 128 * x;
        var posy = 128 * y;

        resultSVGgray += '<image id="tileS' + '_' + 'gray' + '" height="128" width="128" y="'+ posy + '" x="' + posx + '" xlink:href="' + images[16] + '" />\n';

        continue;
      }

      var code = [
        parseInt(topRow[factor * x]),
        parseInt(topRow[factor * x + 2]),
        parseInt(bottomRow[factor * x]),
        parseInt(bottomRow[factor * x + 2])
      ];

      var num = 8 * code[0] + 4 * code[1] + 2 * code[2] + code[3];
      var hex = num.toString(16).toUpperCase();
      var bin = '' + code[0] + code[1] + code[2] + code[3];

      var posx = 128 * x;
      var posy = 128 * y;

      resultSVGwhite += '<image id="tile' + hex + '_' + bin + '" height="128" width="128" y="'+ posy + '" x="' + posx + '" xlink:href="' + images[num] + '" />\n';
      resultSVGgray  += '<image id="tile' + hex + '_' + bin + '" height="128" width="128" y="'+ posy + '" x="' + posx + '" xlink:href="' + images[num] + '" />\n';
    }
  }

  resultSVGwhite += '</svg>\n';
  resultSVGgray  += '</svg>\n';

  downloadSVG('map.svg', 'imageSVGwhite', resultSVGwhite);
  downloadPNG('map.png', 'imagePNGwhite', resultSVGwhite);
  downloadSVG('map_gray.svg', 'imageSVGgray', resultSVGgray);
  downloadPNG('map_gray.png', 'imagePNGgray', resultSVGgray);

  e.preventDefault();
  return false;
});

