from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import random

# Intentar importar las herramientas nativas de Android para abrir apps
try:
    from jnius import autoclass
    from android import activity
    ANDROID_DISPONIBLE = True
except ImportError:
    ANDROID_DISPONIBLE = False

class ProxyTactilApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=25, spacing=15)
        
        # 1. Encabezado estilo Servidor/Proxy
        self.layout.add_widget(Label(
            text='🌐 HACKER PROXY TOUCH v1.1 🌐', 
            font_size='22sp', 
            bold=True,
            color=(0, 1, 0.5, 1), 
            size_hint_y=None, 
            height=40
        ))
        
        self.lbl_servidor = Label(
            text='SERVIDOR: DESCONECTADO (LATENCIA ALTA)', 
            font_size='14sp',
            color=(1, 0, 0, 1)
        )
        self.layout.add_widget(self.lbl_servidor)
        
        # 2. Gran Botón de Encendido / Conexión Proxy
        self.btn_proxy = Button(
            text='⚡ ENLISTAR PROXY (START) ⚡', 
            size_hint_y=None, 
            height=80, 
            background_color=(0, 0.8, 1, 1), 
            font_size='18sp',
            bold=True
        )
        self.btn_proxy.bind(on_press=self.alternar_proxy)
        self.layout.add_widget(self.btn_proxy)
        
        # 3. Consola de Logs
        self.layout.add_widget(Label(text='CONSOLA DE INYECCIÓN TÁCTIL:', font_size='12sp', halign='left', size_hint_y=None, height=20))
        self.consola = TextInput(
            text='[SISTEMA] Esperando activación del Proxy...\n',
            readonly=True,
            background_color=(0.05, 0.05, 0.05, 1),
            foreground_color=(0, 1, 0, 1), 
            font_size='12sp'
        )
        self.layout.add_widget(self.consola)
        
        self.proxy_activo = False
        return self.layout

    def alternar_proxy(self, instance):
        if not self.proxy_activo:
            self.proxy_activo = True
            self.btn_proxy.text = '🛑 APAGAR PROXY (STOP) 🛑'
            self.btn_proxy.background_color = (1, 0, 0.3, 1)
            self.lbl_servidor.text = 'SERVIDOR: PROCESANDO INYECCIÓN...'
            self.lbl_servidor.color = (1, 1, 0, 1)
            
            self.consola.text = "[SISTEMA] Iniciando túnel Proxy Táctil...\n"
            self.contador_logs = 0
            Clock.schedule_interval(self.simular_logs_proxy, 0.4) 
        else:
            self.proxy_activo = False
            Clock.unschedule(self.simular_logs_proxy)
            self.btn_proxy.text = '⚡ ENLISTAR PROXY (START) ⚡'
            self.btn_proxy.background_color = (0, 0.8, 1, 1)
            self.lbl_servidor.text = 'SERVIDOR: DESCONECTADO (LATENCIA ALTA)'
            self.lbl_servidor.color = (1, 0, 0, 1)
            self.consola.text += "[SISTEMA] Proxy detenido. Sensibilidad revertida.\n"

    def simular_logs_proxy(self, dt):
        comandos_hacker = [
            "[OK] Modificando buffer del digitalizador...",
            "[INFO] Escaneando tasa de muestreo del panel táctil...",
            "[OK] Forzando tasa de refresco a máxima capacidad...",
            "[AJUSTE] Fijando supresor interno en 0.7s...",
            "[SUCESO] Optimizando registro de toques en eje Y (Miras)...",
            "[PROXY] Enlazando bypass de latencia táctil...",
            "[CONECTADO] Servidor 'Red_Headshot_Bypass' activo.",
            "[INFO] Estabilizando puntero de Android...",
            "[EXITO] Modificación inyectada correctamente. ¡Pega todo rojo!",
            "[SISTEMA] Ejecutando Free Fire automáticamente..."
        ]
        
        if self.contador_logs < len(comandos_hacker):
            self.consola.text += comandos_hacker[self.contador_logs] + "\n"
            self.contador_logs += 1
        else:
            self.lbl_servidor.text = f"CONECTADO // LATENCIA: {random.randint(12, 28)}ms // BYPASS: ACTIVO"
            self.lbl_servidor.color = (0, 1, 0, 1)
            
            # Programar la apertura del juego 1 segundo después de terminar los logs
            Clock.schedule_once(self.abrir_free_fire, 1.0)
            return False 

    def abrir_free_fire(self, dt):
        # Nombre del paquete oficial de Free Fire en Android
        package_name = "com.dts.freefireth" 
        
        if ANDROID_DISPONIBLE:
            try:
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                currentActivity = PythonActivity.mActivity
                PackageManager = autoclass('android.content.pm.PackageManager')
                pm = currentActivity.getPackageManager()
                
                # Intentar obtener el disparador de inicio del juego
                intent = pm.getLaunchIntentForPackage(package_name)
                if intent is not None:
                    currentActivity.startActivity(intent)
                else:
                    self.consola.text += "[ERROR] Free Fire no está instalado en este dispositivo.\n"
            except Exception as e:
                self.consola.text += f"[ERROR NATIVO] No se pudo abrir el juego: {str(e)}\n"
        else:
            # Mensaje de respaldo si lo pruebas en PC o entornos de prueba básicos
            self.consola.text += f"[PC SIMULACIÓN] Abriendo paquete: {package_name}\n"

if __name__ == '__main__':
    ProxyTactilApp().run()
