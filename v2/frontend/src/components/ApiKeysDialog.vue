<template>
  <Teleport to="body">
    <Transition name="fade">
      <div v-if="modelValue" class="dialog-overlay" @click="close">
        <Transition name="slide-up">
          <div v-if="modelValue" class="dialog" @click.stop>
            <div class="dialog-glow"></div>
            
            <div class="dialog-inner">
              <div class="dialog-header">
                <h2 class="dialog-title">API Keys</h2>
                <button class="silver-close-btn" @click="close" aria-label="Close dialog">
                  <CloseIcon />
                </button>
              </div>
              
              <div class="dialog-body">
                <p class="dialog-description">
                  Configure your API keys to enable S.H.I.V.A's full functionality.
                </p>
                
                <div class="api-key-field">
                  <label class="field-label">OpenAI API Key</label>
                  <div class="field-wrapper">
                    <input
                      type="password"
                      placeholder="sk-..."
                      class="field-input"
                    />
                  </div>
                </div>
                
                <div class="api-key-field">
                  <label class="field-label">Google API Key</label>
                  <div class="field-wrapper">
                    <input
                      type="password"
                      placeholder="AIza..."
                      class="field-input"
                    />
                  </div>
                </div>
                
                <div class="api-key-field">
                  <label class="field-label">News API Key</label>
                  <div class="field-wrapper">
                    <input
                      type="password"
                      placeholder="Your News API key"
                      class="field-input"
                    />
                  </div>
                </div>
              </div>
              
              <div class="dialog-footer">
                <button class="silver-btn cancel-btn" @click="close">Cancel</button>
                <button class="silver-btn save-btn" @click="save">
                  <span class="btn-shimmer"></span>
                  Save Keys
                </button>
              </div>
            </div>
          </div>
        </Transition>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup lang="ts">
import CloseIcon from './icons/CloseIcon.vue'

defineProps<{
  modelValue: boolean
}>()

const emit = defineEmits<{
  (e: 'update:modelValue', value: boolean): void
}>()

const close = () => {
  emit('update:modelValue', false)
}

const save = () => {
  close()
}
</script>

<style scoped>
.dialog-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 24px;
}

.dialog {
  position: relative;
  width: 100%;
  max-width: 480px;
  border-radius: 24px;
  padding: 1px;
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.3) 0%,
    rgba(255, 255, 255, 0.1) 50%,
    rgba(255, 255, 255, 0.2) 100%
  );
  box-shadow: 
    0 24px 64px rgba(0, 0, 0, 0.4),
    0 0 0 1px rgba(255, 255, 255, 0.1);
}

.dialog-glow {
  position: absolute;
  inset: -1px;
  border-radius: 24px;
  background: radial-gradient(ellipse at top, var(--accent-glow) 0%, transparent 60%);
  opacity: 0.5;
  pointer-events: none;
}

.dialog-inner {
  position: relative;
  background: var(--dialog-bg);
  backdrop-filter: blur(40px) saturate(180%);
  -webkit-backdrop-filter: blur(40px) saturate(180%);
  border-radius: 23px;
  padding: 28px;
  transition: var(--transition);
}

.dialog-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.dialog-title {
  font-size: 22px;
  font-weight: 600;
  color: var(--text-primary);
  letter-spacing: -0.02em;
}

.silver-close-btn {
  position: relative;
  width: 32px;
  height: 32px;
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

.silver-close-btn:hover {
  transform: scale(1.08);
  color: var(--text-primary);
  box-shadow: 
    0 0 16px var(--btn-hover-glow),
    0 2px 8px rgba(0, 0, 0, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.dialog-body {
  margin-bottom: 24px;
}

.dialog-description {
  font-size: 14px;
  font-weight: 400;
  color: var(--text-secondary);
  margin-bottom: 24px;
  line-height: 1.5;
}

.api-key-field {
  margin-bottom: 16px;
}

.field-label {
  display: block;
  font-size: 13px;
  font-weight: 500;
  color: var(--text-secondary);
  margin-bottom: 8px;
  letter-spacing: 0.01em;
}

.field-wrapper {
  position: relative;
  border-radius: 12px;
  padding: 1px;
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.2) 0%,
    rgba(255, 255, 255, 0.05) 100%
  );
}

.field-input {
  width: 100%;
  padding: 12px 14px;
  border-radius: 11px;
  border: 1px solid var(--input-border);
  background: var(--input-bg);
  backdrop-filter: blur(10px);
  font-size: 14px;
  font-weight: 400;
  color: var(--text-primary);
  transition: var(--transition);
  outline: none;
}

.field-input::placeholder {
  color: var(--text-muted);
}

.field-input:focus {
  border-color: var(--accent-glow-strong);
  box-shadow: 0 0 0 3px var(--accent-glow), inset 0 1px 0 rgba(255, 255, 255, 0.05);
}

.dialog-footer {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}

.silver-btn {
  position: relative;
  padding: 10px 20px;
  border-radius: 12px;
  border: 1px solid var(--btn-silver-border);
  background: linear-gradient(180deg, var(--btn-silver-start) 0%, var(--btn-silver-end) 100%);
  color: var(--text-primary);
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition);
  overflow: hidden;
  box-shadow: 
    0 1px 2px rgba(0, 0, 0, 0.06),
    inset 0 1px 0 rgba(255, 255, 255, 0.12);
}

.silver-btn:hover {
  transform: scale(1.02);
  box-shadow: 
    0 0 20px var(--btn-hover-glow),
    0 4px 12px rgba(0, 0, 0, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.silver-btn:active {
  transform: scale(0.98);
}

.cancel-btn {
  opacity: 0.8;
}

.save-btn {
  background: linear-gradient(135deg, var(--accent-glow-strong) 0%, var(--accent-glow) 100%);
  color: white;
  border-color: transparent;
}

.save-btn:hover {
  box-shadow: 0 0 24px var(--accent-glow-strong);
}

.btn-shimmer {
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
  background-size: 200% 100%;
  animation: shimmer 3s infinite;
  pointer-events: none;
}

/* Transitions */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.slide-up-enter-from,
.slide-up-leave-to {
  opacity: 0;
  transform: translateY(20px) scale(0.96);
}
</style>
