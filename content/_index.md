<div style="margin-bottom: 0.5em;"></div>
<!-- {{< alert "circle-info" >}}
Actively searching for <b>off-cycle</b> and <b>SU25</b> opportunities
{{< /alert >}} -->

Hey, I'm a **grad student** @ <span class="pop-emoji" data-emoji="🐻" style="cursor:pointer; font-weight:bold;">UCLA</span> and alumnus of <span class="pop-emoji" data-emoji="🐌" style="cursor:pointer; font-weight:bold;">UCSC</span>. I take [**pictures**](https://unsplash.com/@hdadhich01), build [**stuff**](https://github.com/hdadhich01/?tab=repositories) for convenience, and make [**guides**](blog). I enjoy minimalist design, EDC gear, and software for [**productivity**](/tools) and education. Previously interned at [**Intuitive**](https://www.intuitive.com/en-us) and a clinical AI startup.

<script>
(function() {
  function createEmojiBurst(el, emoji) {
    // For special UC Santa Cruz: combo slug+banana
    const isUCSC = el.textContent.trim().toLowerCase().includes("ucsc");
    // If UCSC, alternate 🐌 and 🍌, else use uniform emoji
    const slugBananaCombo = ['🐌','🍌','🐌','🍌','🐌','🍌','🐌','🍌','🐌'];

    const rect = el.getBoundingClientRect();
    const numEmojis = 9;
    const angleStep = 2 * Math.PI / numEmojis;
    const parent = el.offsetParent || document.body;
    for (let i = 0; i < numEmojis; i++) {
      const span = document.createElement('span');
      // UCSC = combo, else uniform emoji
      span.textContent = isUCSC ? slugBananaCombo[i % slugBananaCombo.length] : emoji;
      span.style.position = 'absolute';
      span.style.pointerEvents = 'none';
      span.style.fontSize = '1em'; // Slightly smaller emoji
      span.style.top = (rect.top + rect.height/2 - parent.getBoundingClientRect().top) + 'px';
      span.style.left = (rect.left + rect.width/2 - parent.getBoundingClientRect().left) + 'px';
      // initial state
      span.style.transform = `translate(0px, 0px) scale(1)`;
      span.style.transition = 'transform 1.25s cubic-bezier(.24,.85,.36,1.46), opacity 1.08s';
      span.style.zIndex = '9999';
      span.style.opacity = '1';
      parent.appendChild(span);

      // Animate outwards explosively, then downward with fade
      setTimeout(() => {
        const distance = 58 + Math.random()*24;
        const angle = i * angleStep + (Math.random() - 0.5) * 0.8;
        // Outwards and slight up (explosion)
        const x = Math.cos(angle) * distance;
        const y = Math.sin(angle) * distance * 0.85;
        // Animate to "explosion"
        span.style.transform = `translate(${x}px, ${y}px) scale(1.22)`;
        // After short pause at peak, let it "fall" and fade
        setTimeout(() => {
          // "Fall away" - drift down from peak, increase scale slightly, fade out
          span.style.transition = 'transform 0.85s cubic-bezier(.51,1.26,.66,.87), opacity 0.75s';
          span.style.transform = `translate(${x + (Math.random()-0.5)*16}px, ${y + 55 + Math.random()*23}px) scale(0.94) rotate(${(Math.random() - 0.5)*36}deg)`;
          span.style.opacity = '0';
        }, 320 + Math.random()*90);
      }, 14);

      // Remove after animation
      setTimeout(() => {
        if (span.parentNode === parent) parent.removeChild(span);
      }, 1700);
    }
  }
  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.pop-emoji').forEach(function(el) {
      el.addEventListener('click', function(e) {
        createEmojiBurst(el, el.getAttribute('data-emoji'));
      });
      el.addEventListener('keydown', function(e) {
        if (e.key === "Enter" || e.key === " ") {
          createEmojiBurst(el, el.getAttribute('data-emoji'));
        }
      });
      el.setAttribute('tabindex', '0');
      el.setAttribute('role', 'button');
      el.setAttribute('aria-label', 'Celebrate ' + el.textContent.trim());
      el.style.outline = 'none';
    });
  });
})();
</script>

<style>
.email-copy { user-select: none; }
.email-copy:hover { text-decoration: underline; }
.email-toast {
  position: absolute;
  top: 50%;
  left: var(--toast-left, 50%);
  transform: translate(-50%, -50%) scale(0.96);
  background: rgba(24,24,27,0.95);
  color: #fff;
  /* Make the black box around 'Copied!' bigger and more proportional to the text */
  padding: 0.85em 2.5em; /* proportional and a bit larger than before */
  border-radius: 1.5em; /* proportional, visually balanced */
  font-size: 0.83em;
  line-height: 1.3;
  box-shadow: 0 6px 20px rgba(0,0,0,0.18);
  opacity: 0;
  pointer-events: none;
  transition: opacity 140ms ease, transform 140ms ease;
  white-space: nowrap;
  z-index: 2;
  will-change: transform, opacity, left;
}
.email-toast.show {
  opacity: 1;
  transform: translate(-50%, -50%) scale(1);
}
</style>

<div style="text-align: center; margin-left: 7%;">
  <span style="font-family: Roboto Mono, monospace; font-size: 0.85em; display: inline-block; line-height: 1.6;">
    <span class="email-copy" data-email="me@harshdadhich.com" style="display: inline-block; min-width: 7.5em; position: relative; cursor: pointer;" role="button" tabindex="0" aria-label="Copy email to clipboard">
      <span style="display: inline-block; width: 4.5em; text-align: right;">me</span>
      <span aria-hidden="true" style="display: inline-block; width: 3em;">[at]</span>
      <span style="display: inline-block; min-width: 13em; text-align: left;">harshdadhich.com</span>
      <span class="email-toast"></span>
    </span><br>
    <span class="email-copy" data-email="hdadhich@ucla.edu" style="display: inline-block; min-width: 7.5em; position: relative; cursor: pointer;" role="button" tabindex="0" aria-label="Copy email to clipboard">
      <span style="display: inline-block; width: 4.5em; text-align: right;">hdadhich</span>
      <span aria-hidden="true" style="display: inline-block; width: 3em;">[at]</span>
      <span style="display: inline-block; min-width: 13em; text-align: left;">ucla.edu</span>
      <span class="email-toast"></span>
    </span>
  </span>
</div>

<style>
.email-copy {
  user-select: none;
  border-radius: 9px;
  background: transparent;
  text-decoration: none !important;
  /* Only encompass text, not padding - override spacing below */
  display: inline-flex;
  align-items: center;
  padding: 0 0.25em;
  /* Remove all margin and unnecessary space so bg hugs text */
  margin: 0;
  box-sizing: border-box;
  /* Remove background transition */
  transition: none;
}
.email-copy span {
  /* Minimize their contribution to outdenting the highlight */
  padding: 0;
  margin: 0;
}
.obfuscate-anim {
  font-family: inherit;
  letter-spacing: inherit;
}
/* No hover/focus styling */
</style>

<script>
(function() {
  // Utility: randomize a string but keep spaces in place
  function randomizeText(text) {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    return text.split('').map(c => {
      if (c === ' ') return c;
      return chars.charAt(Math.floor(Math.random() * chars.length));
    }).join('');
  }

  // Enumerate all email-copy spans that are not toast
  function getEmailTextNodes(el) {
    const spans = Array.from(el.querySelectorAll('span'))
      .filter(s => !s.classList.contains('email-toast'));
    return spans;
  }

  const els = document.querySelectorAll('.email-copy');
  els.forEach(el => {
    const email = el.getAttribute('data-email');
    const toast = el.querySelector('.email-toast');

    // Compute exact horizontal midpoint of rendered email glyphs (excludes the toast)
    function setToastCenter() {
      const elRect = el.getBoundingClientRect();

      const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, {
        acceptNode(node) {
          const p = node.parentElement;
          if (!node.textContent || !node.textContent.trim()) return NodeFilter.FILTER_REJECT;
          if (p && p.classList.contains('email-toast')) return NodeFilter.FILTER_REJECT;
          return NodeFilter.FILTER_ACCEPT;
        }
      });

      let left = Infinity, right = -Infinity, n;
      while ((n = walker.nextNode())) {
        const range = document.createRange();
        range.setStart(n, 0);
        range.setEnd(n, n.textContent.length);
        const rects = range.getClientRects();
        if (rects.length) {
          left = Math.min(left, rects[0].left);
          right = Math.max(right, rects[rects.length - 1].right);
        } else {
          const r = range.getBoundingClientRect();
          left = Math.min(left, r.left);
          right = Math.max(right, r.right);
        }
      }

      if (left < right && left !== Infinity) {
        const midpoint = (left + right) / 2 - elRect.left; // px within .email-copy
        el.style.setProperty('--toast-left', midpoint + 'px');
      }
    }

    // Initial calculation and keep updated on font/load/resize
    if (document.fonts?.ready) document.fonts.ready.then(setToastCenter);
    setToastCenter();
    if ('ResizeObserver' in window) {
      const ro = new ResizeObserver(setToastCenter);
      ro.observe(el);
    } else {
      window.addEventListener('resize', setToastCenter);
    }

    // 1. Find spans to obfuscate (all but .email-toast)
    const spans = getEmailTextNodes(el);

    // 2. Store their original textContent, set obfuscate-anim class
    const originals = spans.map(span => {
      span.classList.add('obfuscate-anim');
      return span.textContent;
    });

    let animFrame = null, animating = false, revealTimeout = null;

    // Animate - obfuscate all relevant spans
    function obfuscate() {
      spans.forEach((span, i) => {
        span.textContent = randomizeText(originals[i]);
      });
    }

    function startAnim() {
      if (animating) return;
      animating = true;
      function frame() {
        if (!animating) return;
        obfuscate();
        animFrame = requestAnimationFrame(frame);
      }
      frame();
    }

    function stopAnimAndReveal() {
      animating = false;
      if (animFrame) cancelAnimationFrame(animFrame);
      spans.forEach((span, i) => {
        span.textContent = originals[i];
      });
    }

    function showToast() {
      if (!toast) return;
      setToastCenter(); // ensure midpoint is current before showing
      toast.textContent = 'Copied!';
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 1000);
    }

    async function copy() {
      try {
        await navigator.clipboard.writeText(email);
      } catch (e) {
        const ta = document.createElement('textarea');
        ta.value = email;
        ta.setAttribute('readonly', '');
        ta.style.position = 'absolute';
        ta.style.left = '-9999px';
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
      }
    }

    // The animation should trigger on mouseenter/focus/keydown, stop/reveal after 700ms or on mouseleave/blur/click/copy-done

    function triggerObfuscateAnim() {
      startAnim();
      if (revealTimeout) clearTimeout(revealTimeout);
      revealTimeout = setTimeout(() => {
        stopAnimAndReveal();
      }, 700);
    }

    el.addEventListener('mouseenter', triggerObfuscateAnim);
    el.addEventListener('focus', triggerObfuscateAnim, true);

    el.addEventListener('mouseleave', stopAnimAndReveal);
    el.addEventListener('blur', stopAnimAndReveal, true);

    el.addEventListener('click', () => {
      stopAnimAndReveal();
      copy().finally(showToast);
    });

    el.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        stopAnimAndReveal();
        copy().finally(showToast);
      } else {
        triggerObfuscateAnim();
      }
    });
  });
})();
</script>

{{< button href="https://cal.com/hdadhich01/chat">}}
Let's Chat!
{{< /button >}}
&nbsp;
{{< button href="/resume/latest.pdf" target="_self" >}}
Resume
{{< /button >}}

<!-- 100% privacy-first analytics -->
<script async defer src="https://api.harshdadhich.com/latest.js"></script>

<noscript><img src="https://custom.domain.com/noscript.gif" alt="" referrerpolicy="no-referrer-when-downgrade" /></noscript>
