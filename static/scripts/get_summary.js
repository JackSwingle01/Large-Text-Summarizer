//max char buttons
const get_summary_button = document.querySelector('#get_summary_button');
const input_textarea = document.querySelector('#input_textarea');
const size_selector = document.querySelector('#size_selector')
const output = document.querySelector('#output_p');
const url = 'http://localhost:5000/summarize'

const character_count = {
    'short': 1000,
    'medium': 2000,
    'long': 3000
}


get_summary_button.addEventListener('click', async () => {
    let text = input_textarea.value;
    let size = size_selector.value;
    let summary_size = character_count[size];
    // console.log(size)
    // console.log(summary_size);
    output.innerHTML = 'Summarizing...';
    get_summary_button.disabled = true;
    get_summary_button.innerHTML = 'Wait...';
    let summary = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: text,
            summary_size: summary_size
        })
    });
    let summary_text = await summary.text();
    output.innerHTML = summary_text;
    get_summary_button.disabled = false;
    get_summary_button.innerHTML = 'Get Summary';
});
