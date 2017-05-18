from plistlib import Plist

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = """
InQRy is a cross-platform application that generates a single QR code containing the machine's hardware specifications.
This application is designed primarily to be used during a physical inventory procedure.

The QR code contains detailed information about the client machine or device, which can then be scanned it quickly add
assets into a Snipe-IT database.
"""

version = '1.2.3'

plist = Plist.fromFile('Info.plist')
plist.update(dict(
        CFBundleVersion=version,
        CFBundleShortVersionString=version,
        CFBundleName='InQRy'))

setup(
        name='inqry',
        app=['inqry/__main__.py'],
        author=['Microsoft Apex Lab'],
        author_email='apxlab@microsoft.com',
        description='A cross-platform utility used to generate a QR code containing hardware specs',
        license='MIT',
        long_description=long_description,
        packages=['inqry', 'inqry.system_specs'],
        install_requires=['Pillow',
                          'pytest',
                          'PyYAML',
                          'qrcode',
                          'wmi;platform_system=="Windows"',
                          'pypiwin32;platform_system=="Windows"'],
        tests_require=['pytest'],
        url='https://github.com/Microsoft/InQRy',
        version=version,
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Intended Audience :: Information Technology',
            'Intended Audience :: System Administrators',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3 :: Only'],
        options=dict(
                py2app=dict(
                        plist=plist)))
