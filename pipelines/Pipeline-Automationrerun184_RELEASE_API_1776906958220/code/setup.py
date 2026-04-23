from setuptools import setup, find_packages
setup(
    name = 'Pipeline-Automationrerun184_RELEASE_API_1776906958220',
    version = '1.0',
    packages = (
      find_packages(include = ('pipelineautomationrerun184_release_api_1776906958220*', ))
      + ['prophecy_config_instances.pipelineautomationrerun184_release_api_1776906958220']
    ),
    package_dir = {
      'prophecy_config_instances.pipelineautomationrerun184_release_api_1776906958220': 'configs/resources/pipelineautomationrerun184_release_api_1776906958220'
    },
    package_data = {'prophecy_config_instances.pipelineautomationrerun184_release_api_1776906958220' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.1.17'],
    entry_points = {
'console_scripts' : [
'main = pipelineautomationrerun184_release_api_1776906958220.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
