<template>
  <div class="app" :class="{ dark: isDark }">
    <!-- Background layers -->
    <div class="bg-gradient"></div>
    <div class="bg-noise"></div>
    <div class="floating-shapes">
      <div class="shape shape-1"></div>
      <div class="shape shape-2"></div>
      <div class="shape shape-3"></div>
    </div>

    <!-- Top bar -->
    <header class="top-bar">
      <button class="silver-btn icon-btn" @click="toggleTheme" aria-label="Toggle theme">
        <SunIcon v-if="isDark" />
        <MoonIcon v-else />
      </button>
      <button class="silver-btn api-keys-btn" @click="showApiKeys = true">
        <span class="btn-shimmer"></span>
        API KEYS
      </button>
    </header>

    <!-- Main content -->
    <main class="main-content">
      <!-- Logo section with multicolour aura -->
      <div class="logo-section">
        <div class="aura aura-outer"></div>
        <div class="aura aura-middle"></div>
        <div class="aura aura-inner"></div>
        <div class="logo-wrapper">
          <img
            src="/ui/shiva-dark.png"
            alt="S.H.I.V.A"
            class="mascot"
            @error="handleImageError"
          />
        </div>
      </div>

      <!-- Title with typewriter -->
      <div class="title-section">
        <h1 class="tagline">
          <TypewriterText
            :phrases="phrases"
            :typing-speed="60"
            :deleting-speed="35"
            :pause-duration="3000"
          />
        </h1>
      </div>
    </main>

    <!-- Fixed bottom chat input -->
    <ChatInput />

    <!-- Footer -->
    <footer class="footer">© 2026 S.H.I.V.A</footer>

    <ApiKeysDialog v-model="showApiKeys" />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import ChatInput from './components/ChatInput.vue'
import TypewriterText from './components/TypewriterText.vue'
import SunIcon from './components/icons/SunIcon.vue'
import MoonIcon from './components/icons/MoonIcon.vue'
import ApiKeysDialog from './components/ApiKeysDialog.vue'

const isDark = ref(false)
const showApiKeys = ref(false)

const toggleTheme = () => {
  isDark.value = !isDark.value
}

const phrases = [
  'Your Desktop Assistant At Work',
  'Hello Aditya, I am S.H.I.V.A',
  'Ready to automate your world',
  'Ask me anything, anytime',
  'Your AI, always listening',
  'S.H.I.V.A stands by your side'
]

const handleImageError = (e: Event) => {
  const img = e.target as HTMLImageElement
  console.error('Failed to load image:', img.src)
}
</script>

<style scoped>
.app {
  position: relative;
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--bg-primary);
  color: var(--text-primary);
  transition: var(--transition);
  overflow: hidden;
}

/* Background gradient - animated two-color shift */
.bg-gradient {
  position: fixed;
  inset: 0;
  background: linear-gradient(135deg, var(--bg-gradient-start) 0%, var(--bg-gradient-end) 100%);
  background-size: 400% 400%;
  z-index: 0;
  animation: bg-shift 12s ease infinite;
  transition: var(--transition);
}

@keyframes bg-shift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Noise texture overlay */
.bg-noise {
  position: fixed;
  inset: 0;
  opacity: 0.03;
  z-index: 1;
  pointer-events: none;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-repeat: repeat;
  background-size: 256px 256px;
}

/* Floating shapes */
.floating-shapes {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
}

.shape {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.4;
  animation: drift 20s infinite ease-in-out;
}

.shape-1 {
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, var(--accent-glow) 0%, transparent 70%);
  top: -10%;
  left: -5%;
  animation-delay: 0s;
}

.shape-2 {
  width: 350px;
  height: 350px;
  background: radial-gradient(circle, rgba(139, 92, 246, 0.2) 0%, transparent 70%);
  bottom: -5%;
  right: -5%;
  animation-delay: -7s;
}

.shape-3 {
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(59, 130, 246, 0.15) 0%, transparent 70%);
  top: 40%;
  left: 60%;
  animation-delay: -14s;
}

/* Top bar */
.top-bar {
  position: fixed;
  top: 20px;
  right: 24px;
  display: flex;
  align-items: center;
  gap: 12px;
  z-index: 10;
}

/* Silver metallic button */
.silver-btn {
  position: relative;
  padding: 8px 16px;
  border-radius: 10px;
  border: 1px solid var(--btn-silver-border);
  background: linear-gradient(180deg, var(--btn-silver-start) 0%, var(--btn-silver-end) 100%);
  color: var(--text-primary);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.5px;
  cursor: pointer;
  transition: var(--transition);
  overflow: hidden;
  box-shadow: 
    0 1px 2px rgba(0, 0, 0, 0.08),
    inset 0 1px 0 rgba(255, 255, 255, 0.15);
}

.silver-btn:hover {
  transform: scale(1.02);
  box-shadow: 
    0 0 20px var(--btn-hover-glow),
    0 4px 12px rgba(0, 0, 0, 0.15),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.silver-btn:active {
  transform: scale(0.98);
}

.icon-btn {
  padding: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.btn-shimmer {
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
  background-size: 200% 100%;
  animation: shimmer 3s infinite;
  pointer-events: none;
}

/* Main content */
.main-content {
  position: relative;
  z-index: 2;
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  width: 100%;
  padding: 80px 16px 170px;
}

/* Logo section with multicolour aura */
.logo-section {
  position: relative;
  width: min(600px, 58vmin, calc(100vh - 340px));
  height: min(600px, 58vmin, calc(100vh - 340px));
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 1;
  min-height: 0;
}

.aura {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
}

.aura-outer {
  width: 90%;
  height: 90%;
  background: conic-gradient(
    from 0deg,
    rgba(6, 182, 212, 0.5),
    rgba(139, 92, 246, 0.4),
    rgba(236, 72, 153, 0.4),
    rgba(245, 158, 11, 0.3),
    rgba(34, 197, 94, 0.4),
    rgba(6, 182, 212, 0.5)
  );
  filter: blur(60px);
  animation: aura-rotate 12s linear infinite;
  opacity: 0.7;
}

.aura-middle {
  width: 72%;
  height: 72%;
  background: conic-gradient(
    from 180deg,
    rgba(34, 211, 238, 0.5),
    rgba(168, 85, 247, 0.4),
    rgba(244, 114, 182, 0.4),
    rgba(251, 191, 36, 0.3),
    rgba(52, 211, 153, 0.4),
    rgba(34, 211, 238, 0.5)
  );
  filter: blur(40px);
  animation: aura-rotate 8s linear infinite reverse;
  opacity: 0.6;
}

.aura-inner {
  width: 53%;
  height: 53%;
  background: radial-gradient(
    circle,
    rgba(6, 182, 212, 0.6) 0%,
    rgba(139, 92, 246, 0.3) 40%,
    transparent 70%
  );
  filter: blur(30px);
  animation: pulse-glow 3s ease-in-out infinite;
}

.logo-wrapper {
  position: relative;
  z-index: 2;
  width: 85%;
  height: 85%;
  display: flex;
  align-items: center;
  justify-content: center;
  animation: float 6s infinite ease-in-out;
}

.mascot {
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: drop-shadow(0 12px 40px rgba(0, 0, 0, 0.25));
}

/* Title section */
.title-section {
  text-align: center;
  margin-bottom: 20px;
  min-height: 36px;
  margin-top: 0;
  flex-shrink: 0;
  z-index: 3;
  position: relative;
}

.tagline {
  font-size: clamp(20px, 4vw, 26px);
  font-weight: 600;
  color: var(--text-primary);
  letter-spacing: -0.02em;
  transition: var(--transition);
  padding: 0 16px;
}

/* Footer */
.footer {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 11px;
  font-weight: 400;
  color: var(--text-muted);
  text-align: center;
  z-index: 2;
  letter-spacing: 0.05em;
  transition: var(--transition);
}

/* Mobile responsive */
@media (max-width: 768px) {
  .main-content {
    padding: 64px 12px 150px;
    gap: 16px;
  }
  
  .logo-section {
    width: min(440px, 52vmin, calc(100vh - 300px));
    height: min(440px, 52vmin, calc(100vh - 300px));
  }
  
  .title-section {
    margin-top: 0;
    margin-bottom: 16px;
  }
  
  .top-bar {
    top: 12px;
    right: 12px;
    gap: 8px;
  }
  
  .silver-btn {
    padding: 6px 12px;
    font-size: 11px;
  }
  
  .footer {
    bottom: 12px;
    font-size: 10px;
  }
}

@media (max-width: 480px) {
  .main-content {
    padding: 56px 8px 140px;
    gap: 12px;
  }
  
  .logo-section {
    width: min(340px, 52vmin, calc(100vh - 280px));
    height: min(340px, 52vmin, calc(100vh - 280px));
  }
  
  .title-section {
    margin-top: 0;
    margin-bottom: 12px;
  }
  
  .top-bar {
    top: 8px;
    right: 8px;
    gap: 6px;
  }
}
</style>
