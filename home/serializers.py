from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class StaffTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        if not self.user.is_staff:
            raise AuthenticationFailed("Admin access only.")

        data["is_staff"] = self.user.is_staff
        data["name"] = self.user.get_full_name() or self.user.get_username()
        return data
