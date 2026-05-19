document.addEventListener('DOMContentLoaded', () => {
    // Rating Colours
    const ratings = document.querySelectorAll('.alnright');

    ratings.forEach(el => {
        const value = parseFloat(el.textContent);
        if (value < 2.5) {
            el.style.color = '#ff4d4d';
        } else if (value < 3.5) {
            el.style.color = 'orange';
        }
        else {
            
            el.style.color = '#38fc04';
        }
    });

    // Type colours
    const rows = document.querySelectorAll('table tbody tr');
    const typeColors = {
        'Music':      '#b44ff7', 
        'Musical':    '#d44ff7', 
        'Film':       '#4d9ff7',  
        'Short Film': '#4d9ff7', 
        'Literature': '#f7a84d',  
        'Game':       '#4df77a',  
        'Anime':      '#f74d8a',
        'Manga':      '#f74dbd'
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