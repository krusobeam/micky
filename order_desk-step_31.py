# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: OrderDesk
def switch_profile(self, profile_name: str):
        """Переключение активного профиля пользователя."""
        profiles = {p['name']: p for p in self._profiles}
        if profile_name not in profiles:
            raise ValueError(f"Профиль '{profile_name}' не найден. Доступные: {', '.join(profiles.keys())}")
        current_profile_id = self._current_profile_id if self._current_profile_id else None
        old_data = {
            'id': current_profile_id,
            'name': profile_name,
            'is_active': True,
            'orders': [],
            'payments': [],
            'created_at': datetime.now().isoformat()
        }
        self._profiles[profile_name] = old_data.copy()
        if self._current_profile_id is not None:
            current = next(p for p in self._profiles.values() if p['id'] == self._current_profile_id)
            current.update({'is_active': False, 'orders': [], 'payments': []})
        self._current_profile_id = profiles[profile_name]['id']
        return self._current_profile
