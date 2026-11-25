(function () {
  'use strict';
  var doc = document.documentElement;
  doc.classList.remove('no-js');
  doc.classList.add('js');

  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('site-nav');
  if (btn && nav) {
    var close = function (focusBtn) {
      nav.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
      if (focusBtn) btn.focus();
    };
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) close(true);
    });
    document.addEventListener('click', function (e) {
      if (nav.classList.contains('open') && !nav.contains(e.target) && !btn.contains(e.target)) close(false);
    });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) close(false); });
  }

  var pairs = document.querySelectorAll('[data-node]');
  var set = function (id, on) {
    document.querySelectorAll('[data-node="' + id + '"]').forEach(function (el) { el.classList.toggle('on', on); });
  };
  pairs.forEach(function (el) {
    var id = el.getAttribute('data-node');
    ['mouseenter', 'focus'].forEach(function (ev) { el.addEventListener(ev, function () { set(id, true); }); });
    ['mouseleave', 'blur'].forEach(function (ev) { el.addEventListener(ev, function () { set(id, false); }); });
  });

  var links = Array.prototype.slice.call(document.querySelectorAll('[data-spy] a[href^="#"]'));
  if (links.length && 'IntersectionObserver' in window) {
    var map = {};
    links.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var targets = Object.keys(map).map(function (id) { return document.getElementById(id); }).filter(Boolean);
    var current = null;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) current = en.target.id; });
      if (current && map[current]) {
        links.forEach(function (a) { a.classList.remove('on'); a.removeAttribute('aria-current'); });
        map[current].classList.add('on');
        map[current].setAttribute('aria-current', 'true');
        var sub = map[current].closest('.subnav ul');
        if (sub) {
          var a = map[current];
          var left = a.offsetLeft - sub.clientWidth / 2 + a.clientWidth / 2;
          sub.scrollLeft = left;
        }
      }
    }, { rootMargin: '-25% 0px -65% 0px', threshold: 0 });
    targets.forEach(function (t) { io.observe(t); });
  }

  document.querySelectorAll('a[href^="http"]').forEach(function (a) {
    if (a.hostname !== location.hostname) a.setAttribute('rel', 'noopener');
  });
})();
