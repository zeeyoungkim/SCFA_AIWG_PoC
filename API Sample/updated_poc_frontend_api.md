# 여행 챗앱 프론트엔드 API 명세 (POC용 - DB 스키마 반영)

---

# 🔐 1. 인증 관련 API

## 1.1 전화번호 인증

| Method | Endpoint | 설명 | Request Body | Response |
|--------|----------|------|--------------|----------|
| POST | /api/auth/send-code | 전화번호 인증코드 발송 | `{"phone_number": "010-1234-5678"}` | `{"success": true, "message": "인증코드가 발송되었습니다", "expires_in": 300}` |
| POST | /api/auth/verify-code | 인증코드 확인 및 로그인 | `{"phone_number": "010-1234-5678", "code": "123456"}` | `{"success": true, "token": "jwt_token", "refresh_token": "refresh_token", "user": {"id": 1, "nickname": "여행러버", "country_code": "KOR", "status": "active"}, "is_new_user": false}` |
| POST | /api/auth/refresh | 토큰 갱신 | `{"refresh_token": "refresh_token"}` | `{"success": true, "token": "new_jwt_token", "expires_in": 3600}` |
| POST | /api/auth/logout | 로그아웃 | - | `{"success": true, "message": "로그아웃되었습니다"}` |

---

# 👤 2. 사용자 관리 API

## 2.1 프로필 관리

| Method | Endpoint | 설명 | Request Body | Response |
|--------|----------|------|--------------|----------|
| GET | /api/user/profile | 사용자 프로필 조회 | - | `{"success": true, "data": {"user_id": 1, "nickname": "여행러버", "country_code": "KOR", "status": "active", "created_at": "2025-01-01T00:00:00Z", "updated_at": "2025-01-07T00:00:00Z"}}` |
| PUT | /api/user/profile | 사용자 프로필 수정 | `{"nickname": "새닉네임", "country_code": "JPN"}` | `{"success": true, "message": "프로필이 수정되었습니다", "data": {"nickname": "새닉네임", "country_code": "JPN", "updated_at": "2025-01-07T00:00:00Z"}}` |
| DELETE | /api/user/profile | 회원 탈퇴 | `{"reason": "개인정보보호"}` | `{"success": true, "message": "회원탈퇴가 완료되었습니다"}` |

## 2.2 사용자 설정

| Method | Endpoint | 설명 | Request Body | Response |
|--------|----------|------|--------------|----------|
| GET | /api/user/settings | 사용자 설정 조회 | - | `{"success": true, "data": {"notification_enabled": true, "language": "ko", "settings": {"theme": "light", "auto_translate": false}}}` |
| PUT | /api/user/settings | 사용자 설정 수정 | `{"notification_enabled": false, "language": "en", "settings": {"theme": "dark", "auto_translate": true}}` | `{"success": true, "message": "설정이 저장되었습니다", "data": {"updated_at": "2025-01-07T00:00:00Z"}}` |
| PUT | /api/user/settings/language | 언어 설정 변경 | `{"language": "en"}` | `{"success": true, "message": "언어가 변경되었습니다"}` |
| PUT | /api/user/settings/notification | 알림 설정 변경 | `{"notification_enabled": true}` | `{"success": true, "message": "알림 설정이 변경되었습니다"}` |

---

# 💬 3. 대화방 관리 API

## 3.1 대화방 CRUD

| Method | Endpoint | 설명 | Request Body | Response |
|--------|----------|------|--------------|----------|
| GET | /api/chat/rooms | 대화방 목록 조회 | Query: `?page=1&limit=20&status=active` | `{"success": true, "data": {"rooms": [{"id": 1, "title": "도쿄 여행", "room_type": "travel_chat", "status": "active", "created_at": "2025-01-01T00:00:00Z", "updated_at": "2025-01-07T00:00:00Z", "last_message": {"content": "안녕하세요", "created_at": "2025-01-07T00:00:00Z"}, "message_count": 15}], "pagination": {"page": 1, "limit": 20, "total": 5, "total_pages": 1}}}` |
| POST | /api/chat/rooms | 새 대화방 생성 | `{"title": "파리 여행 계획", "room_type": "travel_chat"}` | `{"success": true, "data": {"room_id": 2, "title": "파리 여행 계획", "room_type": "travel_chat", "status": "active", "created_at": "2025-01-07T00:00:00Z"}, "message": "대화방이 생성되었습니다"}` |
| GET | /api/chat/rooms/{room_id} | 특정 대화방 정보 조회 | - | `{"success": true, "data": {"id": 1, "title": "도쿄 여행", "room_type": "travel_chat", "status": "active", "message_count": 15, "created_at": "2025-01-01T00:00:00Z", "updated_at": "2025-01-07T00:00:00Z"}}` |
| PUT | /api/chat/rooms/{room_id} | 대화방 정보 수정 | `{"title": "새로운 제목"}` | `{"success": true, "message": "대화방 정보가 수정되었습니다", "data": {"updated_at": "2025-01-07T00:00:00Z"}}` |
| DELETE | /api/chat/rooms/{room_id} | 대화방 삭제 | - | `{"success": true, "message": "대화방이 삭제되었습니다"}` |

## 3.2 기본 통계

| Method | Endpoint | 설명 | Request Body | Response |
|--------|----------|------|--------------|----------|
| GET | /api/chat/rooms/stats | 내 대화방 요약 통계 | - | `{"success": true, "data": {"total_rooms": 5, "active_rooms": 3, "total_messages": 150}}` |

---

# 📝 4. 메시지 관리 API

## 4.1 메시지 CRUD

| Method | Endpoint | 설명 | Request Body | Response |
|--------|----------|------|--------------|----------|
| GET | /api/chat/rooms/{room_id}/messages | 메시지 목록 조회 | Query: `?page=1&limit=50&before_id=100` | `{"success": true, "data": {"messages": [{"id": 1, "sender_type": "user", "content": "안녕하세요", "message_type": "text", "metadata": {"source": "mobile"}, "created_at": "2025-01-01T00:00:00Z"}], "pagination": {"page": 1, "limit": 50, "has_more": true}}}` |
| POST | /api/chat/rooms/{room_id}/messages | 메시지 전송 | `{"content": "도쿄 여행 추천해줘", "message_type": "text", "metadata": {"source": "web"}}` | `{"success": true, "data": {"message_id": 123, "created_at": "2025-01-07T00:00:00Z"}, "assistant_response": {"id": 124, "content": "도쿄는 정말 멋진 곳입니다...", "message_type": "text", "created_at": "2025-01-07T00:00:00Z"}}` |
| GET | /api/chat/rooms/{room_id}/messages/{message_id} | 특정 메시지 조회 | - | `{"success": true, "data": {"id": 1, "sender_type": "user", "content": "안녕하세요", "message_type": "text", "metadata": {"source": "mobile"}, "created_at": "2025-01-01T00:00:00Z"}}` |
| DELETE | /api/chat/rooms/{room_id}/messages/{message_id} | 메시지 삭제 | - | `{"success": true, "message": "메시지가 삭제되었습니다"}` |

## 4.2 메시지 피드백

| Method | Endpoint | 설명 | Request Body | Response |
|--------|----------|------|--------------|----------|
| POST | /api/chat/messages/{message_id}/feedback | 메시지 피드백 등록 | `{"feedback_type": "helpful", "rating": 5}` | `{"success": true, "data": {"feedback_id": 1, "created_at": "2025-01-07T00:00:00Z"}, "message": "피드백이 등록되었습니다"}` |
| GET | /api/chat/messages/{message_id}/feedback | 내 피드백 조회 | - | `{"success": true, "data": {"id": 1, "feedback_type": "helpful", "rating": 5, "created_at": "2025-01-07T00:00:00Z"}}` |
| PUT | /api/chat/messages/{message_id}/feedback | 피드백 수정 | `{"feedback_type": "not_helpful", "rating": 2}` | `{"success": true, "message": "피드백이 수정되었습니다"}` |
| DELETE | /api/chat/messages/{message_id}/feedback | 피드백 삭제 | - | `{"success": true, "message": "피드백이 삭제되었습니다"}` |

---

# 📊 5. 피드백 및 지원 API

## 5.1 일반 피드백

| Method | Endpoint | 설명 | Request Body | Response |
|--------|----------|------|--------------|----------|
| POST | /api/feedback | 일반 피드백 제출 | `{"feedback_type": "suggestion", "subject": "기능 개선 제안", "content": "이런 기능이 있으면 좋겠어요", "rating": 4}` | `{"success": true, "data": {"feedback_id": 456, "created_at": "2025-01-07T00:00:00Z"}, "message": "피드백이 제출되었습니다"}` |
| GET | /api/feedback | 내 피드백 목록 조회 | Query: `?page=1&limit=10&status=pending` | `{"success": true, "data": {"feedbacks": [{"id": 456, "feedback_type": "suggestion", "subject": "기능 개선 제안", "status": "pending", "rating": 4, "created_at": "2025-01-07T00:00:00Z", "admin_response": null}], "pagination": {"page": 1, "limit": 10, "total": 3}}}` |
| GET | /api/feedback/{feedback_id} | 특정 피드백 조회 | - | `{"success": true, "data": {"id": 456, "feedback_type": "suggestion", "subject": "기능 개선 제안", "content": "이런 기능이 있으면 좋겠어요", "status": "resolved", "rating": 4, "admin_response": "검토해보겠습니다", "created_at": "2025-01-07T00:00:00Z"}}` |

---

# 🌍 6. 국가 정보 API

| Method | Endpoint | 설명 | Request Body | Response |
|--------|----------|------|--------------|----------|
| GET | /api/countries | 국가 목록 조회 | Query: `?search=한국` | `{"success": true, "data": {"countries": [{"code": "KOR", "name_ko": "대한민국", "name_en": "South Korea", "flag_emoji": "🇰🇷"}]}}` |
| GET | /api/countries/{code} | 특정 국가 정보 조회 | - | `{"success": true, "data": {"code": "KOR", "name_ko": "대한민국", "name_en": "South Korea", "flag_emoji": "🇰🇷"}}` |

---

# ⚙️ 7. 앱 정보 API

## 7.1 공지사항

| Method | Endpoint | 설명 | Request Body | Response |
|--------|----------|------|--------------|----------|
| GET | /api/app/notifications | 앱 공지사항 조회 | Query: `?active=true&priority=high` | `{"success": true, "data": {"notifications": [{"id": 1, "title": "서비스 업데이트 안내", "content": "새로운 기능이 추가되었습니다", "notification_type": "update", "priority": "normal", "is_active": true, "display_from": "2025-01-01T00:00:00Z", "display_until": "2025-01-31T23:59:59Z", "created_at": "2025-01-01T00:00:00Z"}]}}` |
| GET | /api/app/notifications/{notification_id} | 특정 공지사항 조회 | - | `{"success": true, "data": {"id": 1, "title": "서비스 업데이트 안내", "content": "새로운 기능이 추가되었습니다", "notification_type": "update", "priority": "normal"}}` |

## 7.2 앱 상태

| Method | Endpoint | 설명 | Request Body | Response |
|--------|----------|------|--------------|----------|
| GET | /api/health | 서버 상태 확인 | - | `{"status": "healthy", "timestamp": "2025-01-07T00:00:00Z", "version": "1.0.0", "services": {"database": "healthy", "llm": "healthy"}}` |

---

# 🔄 8. WebSocket API (실시간 채팅)

## 8.1 연결 및 이벤트

| Event | Direction | 설명 | Payload |
|-------|-----------|------|---------|
| connect | Client → Server | 웹소켓 연결 | `{"token": "jwt_token", "room_id": 1}` |
| join_room | Client → Server | 대화방 입장 | `{"room_id": 1}` |
| leave_room | Client → Server | 대화방 퇴장 | `{"room_id": 1}` |
| message | Server → Client | 실시간 메시지 수신 | `{"id": 124, "room_id": 1, "sender_type": "assistant", "content": "여행 추천드릴게요", "message_type": "text", "metadata": {}, "created_at": "2025-01-07T00:00:00Z"}` |
| typing | Server → Client | AI 타이핑 상태 | `{"room_id": 1, "is_typing": true}` |
| error | Server → Client | 에러 발생 | `{"error_code": "RATE_LIMIT_EXCEEDED", "message": "메시지 전송 한도를 초과했습니다"}` |

## 8.2 WebSocket 연결 엔드포인트

```
wss://api.travel-chat.com/ws/chat
```

**연결 시 헤더:**
```
Authorization: Bearer {jwt_token}
```

---

# 📋 9. 공통 응답 형태

## 9.1 성공 응답

```json
{
  "success": true,
  "data": {
    // 응답 데이터
  },
  "message": "작업이 성공적으로 완료되었습니다"
}
```

## 9.2 오류 응답

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "입력값이 올바르지 않습니다",
    "details": {
      "field": "phone_number",
      "reason": "올바른 전화번호 형식이 아닙니다"
    }
  }
}
```

## 9.3 페이지네이션 응답

```json
{
  "success": true,
  "data": {
    "items": [...],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 100,
      "total_pages": 5,
      "has_more": true
    }
  }
}
```

---

# 🔐 10. 인증 및 권한

## 10.1 JWT 토큰 사용

**헤더에 포함:**
```
Authorization: Bearer {jwt_token}
```

**토큰 정보:**
- 만료 시간: 1시간
- Refresh Token 만료: 7일
- 자동 갱신 가능

## 10.2 Rate Limit 정보

사용자별 제한:
- API 호출: 1000회/시간
- 메시지 전송: 100회/시간
- 피드백 등록: 10회/시간

**응답 헤더:**
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640995200
```

---

# 📊 11. HTTP 상태 코드

| 코드 | 의미 | 사용 상황 |
|------|------|-----------|
| 200 | OK | 성공적인 요청 |
| 201 | Created | 리소스 생성 성공 |
| 400 | Bad Request | 잘못된 요청 형식 |
| 401 | Unauthorized | 인증 실패 또는 토큰 만료 |
| 403 | Forbidden | 권한 없음 |
| 404 | Not Found | 리소스 없음 |
| 422 | Unprocessable Entity | 유효성 검사 실패 |
| 429 | Too Many Requests | Rate Limit 초과 |
| 500 | Internal Server Error | 서버 내부 오류 |

---

# 🧪 12. 개발 환경

## 12.1 API Base URL

| 환경 | Base URL |
|------|----------|
| Development | `https://dev-api.travel-chat.com` |
| Staging | `https://staging-api.travel-chat.com` |
| Production | `https://api.travel-chat.com` |

---

# 📝 13. 주요 변경사항 (DB 스키마 반영)

## 13.1 보안 강화
- 전화번호와 닉네임은 서버에서 암호화 저장
- API 응답에서는 복호화된 형태로 제공

## 13.2 메타데이터 활용
- 메시지에 `metadata` 필드 추가 (소스, 추가 정보 등)
- 사용자 설정에 `settings` 객체 추가 (확장 가능한 설정)

## 13.3 피드백 시스템 강화
- 메시지별 피드백 시스템 추가
- 일반 피드백과 메시지 피드백 분리
- 관리자 응답 필드 추가

## 13.4 타임스탬프 일관성
- 모든 생성/수정 시간은 ISO 8601 형식
- Timezone 정보 포함 (UTC 기준)

---

이 업데이트된 POC용 프론트엔드 API는 새로운 DB 스키마를 반영하여 보안성과 확장성을 고려하면서도 POC 단계에 적합하도록 설계되었습니다.