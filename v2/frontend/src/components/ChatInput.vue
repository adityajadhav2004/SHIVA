<template>
  <div class="chat-container">
    <div class="chat-glass" :class="{ focused: isFocused }">
      <!-- Gradient border effect -->
      <div class="glass-border"></div>
      
      <div class="glass-inner">
        <input
          ref="inputRef"
          type="text"
          v-model="text"
          :maxlength="maxLength"
          placeholder="Hey Aditya, let's work on your ideas"
          class="chat-input"
          @focus="isFocused = true"
          @blur="isFocused = false"
        />
        
        <div class="char-count">{{ text.length }}/{{ maxLength }}</div>
        
        <div class="toolbar">
          <div class="toolbar-left">
            <button class="silver-icon-btn" aria-label="Sparkle">
              <SparkleIcon />
            </button>
            <button class="silver-icon-btn" aria-label="Attach file">
              <PaperclipIcon />
            </button>
            <button class="silver-icon-btn" aria-label="Voice input">
              <MicrophoneIcon />
            </button>
          </div>
          
          <button 
            class="silver-icon-btn send-btn" 
            :class="{ active: text.trim() }"
            :disabled="!text.trim()" 
            aria-label="Send"
          >
            <SendIcon />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import SparkleIcon from './icons/SparkleIcon.vue'
import PaperclipIcon from './icons/PaperclipIcon.vue'
import MicrophoneIcon from './icons/MicrophoneIcon.vue'
import SendIcon from './icons/SendIcon.vue'

const text = ref('')
const maxLength = 500
const isFocused = ref(false)
const inputRef = ref<HTMLInputElement | null>(null)
</script>

<style scoped>
.chat-container {
  position: fixed;
  bottom: 64px;
  left: 50%;
  transform: translateX(-50%);
  width: 100%;
  max-width: 720px;
  padding: 0 24px;
  z-index: 50;
}

/* Glassmorphism outer shell */
.chat-glass {
  position: relative;
  border-radius: 20px;
  padding: 1px;
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.2) 0%,
    rgba(255, 255, 255, 0.05) 50%,
    rgba(255, 255, 255, 0.15) 100%
  );
  box-shadow: 
    0 8px 32px var(--glass-shadow),
    0 0 0 1px var(--glass-border),
    inset 0 1px 0 rgba(255, 255, 255, 0.1);
  transition: var(--transition);
}

.chat-glass.focused {
  box-shadow: 
    0 8px 32px var(--glass-shadow),
    0 0 0 1px var(--accent-glow),
    0 0 40px var(--accent-glow),
    inset 0 1px 0 rgba(255, 255, 255, 0.15);
}

.glass-border {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  padding: 1px;
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.3) 0%,
    transparent 40%,
    transparent 60%,
    rgba(255, 255, 255, 0.2) 100%
  );
  -webkit-mask: 
    linear-gradient(#fff 0 0) content-box, 
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}

.glass-inner {
  position: relative;
  background: var(--glass-bg);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-radius: 19px;
  padding: 16px 20px;
  transition: var(--transition);
}

.chat-input {
  width: 100%;
  border: none;
  outline: none;
  background: transparent;
  font-size: 15px;
  font-weight: 400;
  color: var(--text-primary);
  padding: 0;
  margin-bottom: 8px;
  letter-spacing: 0.01em;
  transition: var(--transition);
}

.chat-input::placeholder {
  color: var(--text-muted);
  font-weight: 300;
}

.char-count {
  font-size: 11px;
  font-weight: 500;
  color: var(--text-muted);
  margin-bottom: 12px;
  user-select: none;
  letter-spacing: 0.02em;
  transition: var(--transition);
}

.toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.toolbar-left {
  display: flex;
  align-items: center;
  gap: 8px;
}

/* Silver metallic icon buttons */
.silver-icon-btn {
  position: relative;
  width: 34px;
  height: 34px;
  border-radius: 10px;
  border: 1px solid var(--btn-silver-border);
  background: linear-gradient(180deg, var(--btn-silver-start) 0%, var(--btn-silver-end) 100%);
  color: var(--text-secondary);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition);
  box-shadow: 
    0 1px 2px rgba(0, 0, 0, 0.06),
    inset 0 1px 0 rgba(255, 255, 255, 0.12);
}

.silver-icon-btn:hover {
  transform: scale(1.08);
  color: var(--text-primary);
  box-shadow: 
    0 0 16px var(--btn-hover-glow),
    0 2px 8px rgba(0, 0, 0, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.silver-icon-btn:active {
  transform: scale(0.95);
}

.send-btn {
  width: 36px;
  height: 36px;
  border-radius: 12px;
  opacity: 0.5;
  transition: var(--transition);
}

.send-btn.active {
  opacity: 1;
  background: linear-gradient(135deg, var(--accent-glow-strong) 0%, var(--accent-glow) 100%);
  color: white;
  border-color: transparent;
}

.send-btn.active:hover {
  transform: scale(1.08);
  box-shadow: 0 0 20px var(--accent-glow-strong);
}

.send-btn:disabled {
  cursor: default;
}

/* Mobile responsive */
@media (max-width: 768px) {
  .chat-container {
    bottom: 48px;
    padding: 0 16px;
  }
  
  .chat-glass {
    border-radius: 16px;
  }
  
  .glass-inner {
    padding: 12px 16px;
  }
  
  .chat-input {
    font-size: 14px;
    margin-bottom: 6px;
  }
  
  .char-count {
    font-size: 10px;
    margin-bottom: 8px;
  }
  
  .toolbar-left {
    gap: 4px;
  }
  
  .silver-icon-btn {
    width: 30px;
    height: 30px;
    border-radius: 8px;
  }
  
  .send-btn {
    width: 32px;
    height: 32px;
  }
}

@media (max-width: 480px) {
  .chat-container {
    bottom: 36px;
    padding: 0 12px;
  }
  
  .glass-inner {
    padding: 10px 14px;
    border-radius: 14px;
  }
  
  .chat-glass {
    border-radius: 14px;
  }
  
  .chat-input {
    font-size: 13px;
  }

  .silver-icon-btn {
    width: 28px;
    height: 28px;
  }

  .send-btn {
    width: 30px;
    height: 30px;
  }
}
</style>
