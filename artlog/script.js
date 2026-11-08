document.addEventListener('DOMContentLoaded', () => {
    // Rating colours
    document.querySelectorAll('.alnright').forEach(el => {
        const value = parseFloat(el.textContent);
        if (isNaN(value)) return; // e.g. "?/?" stays white

        if (value < 2.5) {
            el.style.color = '#ff4d4d';
        } else if (value < 3.5) {
            el.style.color = 'orange';
        } else {
            el.style.color = '#38fc04';
        }
    });

    // Type colours
    const typeColors = {
        'Music':       '#b44ff7',
        'Musical':     '#d44ff7',
        'Film':        '#4d9ff7',
        'Short Film':  '#00beff',
        'Documentary': '#00d7ea',
        'Short Story': '#ff8700',
        'Novel':       '#ff0000',
        'Game':        '#4df77a',
        'Anime':       '#f74d8a',
        'Manga':       '#f74dbd'
    };

    document.querySelectorAll('table tbody tr').forEach(row => {
        const firstCell = row.cells[0];
        if (!firstCell) return;
        const type = firstCell.textContent.trim();
        if (typeColors[type]) {
            firstCell.style.color = typeColors[type];
        }
    });
});

// Which row types each filter button shows
const filterGroups = {
    Film:       ['Film', 'Short Film', 'Documentary'],
    Music:      ['Music', 'Musical'],
    Animanga:   ['Anime', 'Manga'],
    Literature: ['Novel', 'Short Story', 'Poem']
};

// Buttons for hiding types
function filterType(type, btn) {
    const allowed = filterGroups[type] || [type];

    document.querySelectorAll('table tbody tr').forEach(row => {
        if (!row.cells[0]) return;
        const rowType = row.cells[0].textContent.trim();
        row.style.display = (type === 'all' || allowed.includes(rowType)) ? '' : 'none';
    });

    document.querySelectorAll('.filter-buttons button').forEach(b => {
        b.classList.toggle('active', b === btn);
    });
}