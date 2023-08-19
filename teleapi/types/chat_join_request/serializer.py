from teleapi.core.orm.serializers.generics.serializers import ModelSerializer
from teleapi.core.orm.serializers.generics.fields import RelatedSerializerField
from .obj import ChatJoinRequest
from teleapi.types.user import UserSerializer
from teleapi.types.chat_invite_link import ChatInviteLinkSerializer


class ChatJoinRequestSerializer(ModelSerializer):
    user = RelatedSerializerField(UserSerializer(), read_name='from')
    invite_link = RelatedSerializerField(ChatInviteLinkSerializer(), is_required=False)

    class Meta:
        model = ChatJoinRequest
