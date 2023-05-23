// VARIABLES
const saveInputBtn = document.getElementById('saveInput-btn');
const saveTabBtn = document.getElementById('saveTab-btn');
const resetBtn = document.getElementById('reset-btn');
const leadsListEl = document.getElementById('leadsList-el');
const input = document.getElementById('input-el');
const removeBtn = document.getElementById('remove-btn');

let leads = [];


// FUNCTIONS
function render() {
    if (localStorage.getItem('myLeads') != null){
        x = JSON.parse(localStorage.getItem('myLeads'));
        leadsListEl.innerHTML = '';
        leads = [];
        for (let lead of x) {
            leads.push(lead)
            leadsListEl.innerHTML += `
            <li>
                <a href='${lead}' target='_blank' style='color:green'>${lead}
                </a>
            </li>
            <br />`;
        }
    }
}

// BUTTONS
saveInputBtn.addEventListener('click', function() {
    if (input.value != '') {
        leads.push(input.value);
        localStorage.setItem('myLeads', JSON.stringify(leads));
        input.value='';
        render();
    }
})

saveTabBtn.addEventListener('click', function() {

    chrome.tabs.query({active: true, currentWindow: true}, function(activeTab){
        leads.push(activeTab[0].url)
        localStorage.setItem('myLeads', JSON.stringify(leads))
        render()
    })

})

resetBtn.addEventListener('click', function(){
    input.value = '';
    leadsListEl.innerHTML = '';
    localStorage.clear();
    leads = [];
})

render();
