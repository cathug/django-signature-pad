import logging, subprocess
from setuptools import Command
from setuptools.command.build import SubCommand
from setuptools import setup

# set up logger
logger = logging.get_logger(__name__)


class NPMInstallPackages(Command):
    '''
    Use NPM to build javascript components
    '''

    description = 'Class to install NPM packages'


    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


    def run(self):
        logger.info('Installing npm packages.')
        command = 'npm install package.json'.split(' ')
         # if check == True and non-zero exit, raise CalledProcessError
        subprocess.run(command, check=True)

# ------------------------------------------------------------------------------

class NPMBuild(Command):
    '''
    Use npm to compile assets
    '''
    description = 'Class to compile assets'

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        logger.info('Building js and css assets')
        command = 'npm run build-prod'.split(' ')
        # if check == True and non-zero exit, raise CalledProcessError
        subprocess.run(command, check=True)



