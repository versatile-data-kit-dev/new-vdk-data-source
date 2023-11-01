from typing import List
from vdk.api.plugin.hook_markers import hookimpl
from vdk.api.plugin.plugin_registry import IPluginRegistry


from vdk.internal.core.context import CoreContext
from vdk.internal.core.config import ConfigurationBuilder
from vdk.plugin.{{cookiecutter.__plugin_module_name}}.data_source import {{cookiecutter.__plugin_source_class_name}}DataSource


class DataSourcePlugin:

    @hookimpl
    def vdk_data_sources_register(self,
                                  data_source_factory: IDataSourceFactory):
        data_source_factory.register_data_source_class({{cookiecutter.__plugin_source_class_name}}DataSource)


@hookimpl
def vdk_start(plugin_registry: IPluginRegistry, command_line_args: List):
    plugin_registry.load_plugin_with_hooks_impl(DataSourcePlugin(), "DataSource{{cookiecutter.__plugin_source_class_name}}")



