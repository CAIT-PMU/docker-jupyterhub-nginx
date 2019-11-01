# The proxy is in another container
c.ConfigurableHTTPProxy.should_start = False
#c.ConfigurableHTTPProxy.api_url = 'http://proxy:8000'
c.ConfigurableHTTPProxy.api_url = 'http://proxy:8001'
# tell the hub to use Dummy Auth (for testing)
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

# The Hub should listen on all interfaces,
# so user servers can connect
c.JupyterHub.hub_ip = '0.0.0.0'
# Allow ipv6 instead
#c.JupyterHub.hub_ip = '0.0.0.0:8000'

# this is the name of the 'service' in docker-compose.yml
c.JupyterHub.hub_connect_ip = 'pavement-hub'
# this is the network name for jupyterhub in docker-compose.yml
# with a leading 'swarm_' that docker-compose adds
#c.SwarmSpawner.network_name = 'swarm_jupyterhub-net'
c.SwarmSpawner.network_name = 'pavement-hub_jupyterhub-net'

# start jupyterlab
c.Spawner.cmd = ["jupyter", "labhub"]

# debug-logging for testing
import logging
c.JupyterHub.log_level = logging.DEBUG


# use SwarmSpawner
#c.JupyterHub.spawner_class = 'dockerspawner.SwarmSpawner'

from dockerspawner import DockerSpawner

class DemoFormSpawner(DockerSpawner):
    def _options_form_default(self):
        default_stack = "jupyter/minimal-notebook"
        return """
        <label for="stack">Select your desired stack</label>
        <select name="stack" size="1">
        <option value="jupyter/r-notebook">R: </option>
        <option value="jupyter/tensorflow-notebook">Tensorflow: </option>
        <option value="jupyter/datascience-notebook">Datascience: </option>
        <option value="jupyter/all-spark-notebook">Spark: </option>
        </select>
        """.format(stack=default_stack)

    def options_from_form(self, formdata):
        options = {}
        options['stack'] = formdata['stack']
        container_image = ''.join(formdata['stack'])
        print("SPAWN: " + container_image + " IMAGE" )
        self.container_image = container_image
        return options

c.JupyterHub.spawner_class = DemoFormSpawner
