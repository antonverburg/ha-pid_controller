"""The PID controller integration."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from .const import DOMAIN, PLATFORMS, SERVICE_ENABLE, ATTR_VALUE
from homeassistant.helpers.typing import ConfigType
from homeassistant.helpers import service
from homeassistant.helpers.entity_platform import DATA_ENTITY_PLATFORM
import homeassistant.helpers.config_validation as cv
import voluptuous as vol


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up slow PID Controller from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    entry.async_on_unload(entry.add_update_listener(config_entry_update_listener))
    return True


async def config_entry_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Update listener.

    Called when the config entry options are changed.
    """
    await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)


# pylint: disable=unused-argument
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Register services for PID entities."""

    @service.verify_domain_control(hass, DOMAIN)
    async def async_service_handle(service_call: ServiceCall) -> None:
        """Handle services.

        Dispatch the right service call to the right entity.
        """
        # Next code will do a service call to all entities in the
        # current domain that contain the entitiy_id form service_call data
        # hass.data will get all available platforms in this domain.
        await service.entity_service_call(
            hass,
            list(hass.data[DATA_ENTITY_PLATFORM][DOMAIN]),
            "async_" + service_call.service,
            service_call,
        )

    hass.services.async_register(
        DOMAIN,
        SERVICE_ENABLE,
        async_service_handle,
        cv.make_entity_service_schema({vol.Required(ATTR_VALUE): vol.Coerce(bool)}),
    )
    return True
