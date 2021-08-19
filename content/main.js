function change(name) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent margin-bottom" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById('div-' + name).style.display = "block";
}

function openTab(evt, name) {
  change(name);
  evt.currentTarget.className += " active";
  pushUrl('#' + name);
}

function popstate(state) {
  change(state.currentTarget.location.hash.replace('#', ''))
}
window.addEventListener('popstate', popstate);
const pushUrl = (href) => {
  history.pushState({}, '', href);
  console.log(href)
  window.dispatchEvent(new Event('popstate'));
};

function loadLocation() {

  const links = ['#home', '#projects', '#skills', '#work', '#education', '#contact'];
  console.log(links.includes(location.hash))
  if (location.hash == undefined) {
    pushUrl('#home');
  } else if (links.includes(location.hash)) {
    pushUrl(location.hash);
  }
}

// alert(pushUrl('#home'));
