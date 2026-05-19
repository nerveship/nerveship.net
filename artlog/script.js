document.addEventListener('DOMContentLoaded', () => {
    // Rating Colours
    const ratings = document.querySelectorAll('.alnright');

    ratings.forEach(el => {
        const value = parseFloat(el.textContent);
        if (value < 2.5) {
            el.style.color = '#ff4d4d';
        } else if (value < 4) {
            el.style.color = 'orange';
        }
        else {
            
            el.style.color = '#38fc04';
        }
    });

    // Type colours
    const rows = document.querySelectorAll('table tbody tr');
    const typeColors = {
        'Music':      '#b44ff7',  // purple
        'Film':       '#4d9ff7',  // blue
        'Short Film': '#4d9ff7',  // blue (same as film)
        'Literature': '#f7a84d',  // amber
        'Game':       '#4df77a',  // green
        'Anime':      '#f74d8a',  // pink/rose
    };

    rows.forEach(row => {
        if (!row.cells[0]) return;
        const firstCell = row.cells[0];
        const type = firstCell.textContent.trim();
        
        if (typeColors[type]) {
            firstCell.style.color = typeColors[type];
        }
    });
});