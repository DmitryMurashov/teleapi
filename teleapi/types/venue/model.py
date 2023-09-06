from typing import Optional
from teleapi.core.orm.models import Model
from teleapi.core.orm.models.generics.fields import StringModelField, RelatedModelField
from teleapi.types.location import Location


class VenueModel(Model):
    location: Location = RelatedModelField(Location)
    title: str = StringModelField()
    address: str = StringModelField()
    foursquare_id: Optional[str] = StringModelField(is_required=False)
    foursquare_type: Optional[str] = StringModelField(is_required=False)
    google_place_id: Optional[str] = StringModelField(is_required=False)
    google_place_type: Optional[str] = StringModelField(is_required=False)
