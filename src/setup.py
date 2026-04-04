from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.AutoResolution'
setup(name='enigma2-plugin-systemplugins-autoresolution',
       version='3.0',
       description='Automatically change resolution',
       package_dir={pkg: 'AutoResolution'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'maintainer.info']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
