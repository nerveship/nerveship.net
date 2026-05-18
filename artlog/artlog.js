document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.alnright').forEach(cell => {
    const text = cell.textContent.trim();
    const match = text.match(/^([\d.]+)\/5/);
    if (!match) return;
    const score = parseFloat(match[1]);
    if (score <= 2.5) {
      cell.style.color = '#ff3b3b';
      //cell.style.textShadow = '0 0 8px #ff3b3b';
    } else if (score <= 3.5) {
      cell.style.color = '#ffaa00';
      //cell.style.textShadow = '0 0 8px #ffaa00';
    } else {
      cell.style.color = '#38fc04';
      //cell.style.textShadow = '0 0 8px #38fc04';
    }
  });

  const typeColors = {
    'Film':       '#00aaff',
    'Short Film': '#00aaff',
    'Game':       '#38fc04',
    'Music':      '#ff6eb4',
    'Album':      '#ff6eb4',
    'Anime':      '#ffaa00',
    'Manga':      '#ffaa00',
    'Literature': '#00e87a',
    'Musical':    '#ff6eb4',
  };

  document.querySelectorAll('#myTable tbody tr').forEach(row => {
    const typeCell = row.querySelector('td:first-child');
    if (!typeCell) return;
    const type = typeCell.textContent.trim();
    const color = typeColors[type];
    if (color) {
      typeCell.style.color = color;
      //typeCell.style.textShadow = '0 0 8px ' + color;
    }
  });
});