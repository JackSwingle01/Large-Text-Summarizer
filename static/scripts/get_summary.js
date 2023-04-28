//max char buttons
const get_summary_button = document.querySelector('#get_summary_button');
const input_textarea = document.querySelector('#input_textarea');
const summary_size = document.querySelector('#size_selector')
const output = document.querySelector('#output_p');
const url = 'http://localhost:5000/summarize'
get_summary_button.addEventListener('click', async () => {
    let text = input_textarea.value;
    let summary = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: text
        })
    });
    let summary_text = await summary.text();
    output.innerHTML = summary_text;
});
