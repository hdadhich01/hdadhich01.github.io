---
title: "Tools"
layout: "simple"
description: "Some apps for daily drivers, others for occasional utility"
---

Some daily drivers, others for occasional utility

<style>
.tools-img { width: 50%; }
@media (max-width: 640px) { .tools-img { width: 100%; } }

/* hover-to-reveal emoji + tooltip bubble */
.emoji-tip {
  position: relative;
  display: inline-block;
  cursor: help;
  outline: none;
}
/* resting state is full colour; the shared .pulse-egg driver in
   layouts/partials/extend-footer.html flashes it to greyscale */
.emoji-tip-face {
  display: inline-block;
}
/* !important so a hover always beats an in-flight pulse */
.emoji-tip:hover .emoji-tip-face,
.emoji-tip:focus .emoji-tip-face,
.emoji-tip:focus-within .emoji-tip-face {
  filter: grayscale(0) !important;
  opacity: 1 !important;
  transform: scale(1.2);
}

.emoji-tip::after {
  content: attr(data-tip);
  position: absolute;
  bottom: calc(100% + 0.6em);
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  width: max-content;
  max-width: min(20rem, 68vw);
  background: rgba(24, 24, 27, 0.95);
  color: #fff;
  font-size: 0.72rem;
  font-weight: 400;
  line-height: 1.45;
  text-align: center;
  padding: 0.6em 0.85em;
  border-radius: 0.7em;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.18);
  opacity: 0;
  pointer-events: none;
  transition: opacity 160ms ease, transform 160ms ease;
  z-index: 30;
}
.emoji-tip::before {
  content: "";
  position: absolute;
  bottom: calc(100% + 0.2em);
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  border: 5px solid transparent;
  border-top-color: rgba(24, 24, 27, 0.95);
  opacity: 0;
  pointer-events: none;
  transition: opacity 160ms ease, transform 160ms ease;
  z-index: 30;
}
.emoji-tip:hover::after,
.emoji-tip:focus::after,
.emoji-tip:focus-within::after,
.emoji-tip:hover::before,
.emoji-tip:focus::before,
.emoji-tip:focus-within::before {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}
</style>

<div class="tools-img">
  <img src="setup.jpeg" width="100%" style="border-radius: 8px;"/>
  <figcaption style="margin-top: -25px; font-size: 0.75em; text-align: center;">as of during grad school; refresh coming soon</figcaption>
</div>

I like to think these are the best picks given price + value + competition

I've spent a lot of time (much better spent elsewhere) on my picks here

Pieced together from running myself + reddit + [this](https://docs.google.com/spreadsheets/d/1mPuOq3x0SMjmcrrjNpbMqb_ThRc9S51LPD-lnd9ArY4/edit?gid=849549547#gid=849549547)

Check out [this](#subs) to see what I pay for

## Workflow

- [Helium](https://helium.computer) (browser)
  - Optimized for <span style="font-family:SF Pro,Segoe UI Emoji,Apple Color Emoji;">&#63743;</span> + <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Google_Chrome_icon_%28February_2022%29.svg/1280px-Google_Chrome_icon_%28February_2022%29.svg.png" alt="Chrome" title="Chrome" style="height:1em;vertical-align:-0.1em;margin:0 0.1em;display:inline;"> extensions
  - tried [Orion](https://orionbrowser.com) (WebKit-based but buggy ext support)
  - and before that: [Zen](https://zen-browser.app) (Gecko-based but mem heavy)
- [Shortwave](https://shortwave.com) (smart email, just on iOS)
- [Fantastical](https://flexibits.com/fantastical) (calendar)
- [Todoist](https://todoist.com) (todo list, syncs with \^)
- [Obsidian](https://obsidian.md) (`.md` based editor)
  - look at my [.obsidian](https://github.com/hdadhich01/.obsidian) (similar to dotfiles)
- [Buffer](https://samirpatil2000.github.io/products/buffer/) (clipboard manager)
- [WARP](https://1.1.1.1) (privacy for public wifi)
- [Anarlog](https://github.com/fastrepl/hyprnote) (meeting notes; [Granola](https://granola.ai) alt)
- [Scira](https://scira.ai) (deep web search agent)

## Dev

- [Orca](https://www.onorca.dev) ([ADE](https://nimbalyst.com/blog/what-is-an-agentic-development-environment/))
  - used [cmux](https://cmux.com/) before (more of a terminal multiplexer GUI)
  - and good old terminal or VSCode extensions for CC/Codex
- [OrbStack](https://orbstack.dev) (quick VMs/docker)
- [Zed](https://zed.dev) (plain IDE; granular edits ig)
- [Tower](https://www.git-tower.com) (git history GUI; looks cool let me larp)
- [WakaTime](https://wakatime.com) (time tracking; [me](https://wakatime.com/hdadhich01))

## Lifestyle

- [Apple Music](https://music.apple.com) (<span class="emoji-tip" tabindex="0" role="button" aria-label="UI > spotify, algo ≈ spotify" data-tip="UI > spotify, algo ≈ spotify"><span class="emoji-tip-face pulse-egg" data-pulse="desaturate">🫩</span></span>)
- [Origin](https://useorigin.com) (finances dash)
- Health
  - [Hevy](https://www.hevyapp.com) (lifting tracker)
  - [Strava](https://www.strava.com) (cardio tracker)
  - [SuppCo](https://supp.co) (supplement recs)
  - [Yuka](https://yuka.io) (food/cosmetics ratings)
  - [Countoura](https://apps.apple.com/us/app/3d-body-measurement-tracker/id6749202389) (measurements)
  - data from above → claude → insights
- Transport
  - [Transit](https://transit.app) (public transit ETAs)
  - [GasBuddy](https://www.gasbuddy.com) (gas prices)
  - [SpotAngels](https://www.spotangels.com) (street parking finder)
  - [SpotHero](https://spothero.com) (big city cheap parking)
  - [Empower](https://apps.apple.com/us/app/empower-your-ride-your-way/id1454849875) (cheap uber/lyft)
  - [seats.aero](https://seats.aero) (cheap flights; use as mcp)

## Miscellaneous

unnecessary; \*super worth imo

- \*[Swish](https://highlyopinionated.co/swish) (window tiling)
- \*[Hand Mirror](https://handmirror.app) (webcam peek)
- \*[CleanShot X](https://cleanshot.com) (screenshot tool)
- \*[Emoogle](https://www.emoogle.org) (emoji picker)
- [Keka](https://www.keka.io) (archive/compression)
- [Numi](https://numi.app) (NLP calculator)
- [ColorSlurp](https://colorslurp.com) (color picker)
- [Phoenix Slides](https://blyt.net/phxslides/) (SD card viewer)
- [Amphetamine](https://apps.apple.com/us/app/amphetamine/id937984704) (`caffeinate` GUI)
- [CleanMyKeyboard](https://apps.apple.com/us/app/cleanmykeyboard/id6468120888) (disable keyboard)
- [Mos](https://mos.caldis.me) (mouse configurator)
- [Pearcleaner](https://pearcleaner.com) (filesys janitor)
- [Remote Mouse](https://www.remotemouse.net/) (control mouse from phone)

## Digital Subs {#subs}

I freemaxx except these:

Recurring:
- [Apple Music](https://music.apple.com) ($7/m; use edu email)
- [Origin](https://useorigin.com) ($1/y; use limited promo & insta-cancel)
- [Scira Pro](https://scira.ai) ($5/m; use `SCIRASTUD` discount)
- [Claude Pro](https://claude.ai) ($20/m)
- [x.com](https://x.com) ($8/m)

Once:
- [Swish](https://highlyopinionated.co/swish) ($10/life; email for student promo)
- [CleanShot X](https://cleanshot.com) ($20/life; use edu email)

[Tower](https://www.git-tower.com) free through [GitHub Student](https://education.github.com/pack)
