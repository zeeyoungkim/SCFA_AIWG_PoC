# 여행 추천 채팅앱 DB 스키마 (POC용 + Future Work)

---

# 📋 1. 업체 공유 스키마 (프론트엔드 API용 - 고정)

## 1.1 사용자 관리

### users
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | BIGSERIAL | PRIMARY KEY | 사용자 고유 ID |
| phone_number_encrypted | TEXT | NOT NULL | 암호화된 전화번호 |
| phone_number_hash | VARCHAR(64) | NOT NULL UNIQUE | 전화번호 해시값 (검색용) |
| status | VARCHAR(20) | DEFAULT 'active' | 사용자 상태 (active, inactive, banned) |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |
| updated_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 수정일시 |

### user_profiles
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| user_id | BIGINT | PRIMARY KEY REFERENCES users(id) | 사용자 ID |
| nickname_encrypted | TEXT | | 암호화된 닉네임 |
| country_code | VARCHAR(3) | | 선택한 국가 코드 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |
| updated_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 수정일시 |

## 1.2 대화 관리

### chat_rooms
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | BIGSERIAL | PRIMARY KEY | 대화방 고유 ID |
| user_id | BIGINT | NOT NULL REFERENCES users(id) | 사용자 ID |
| title | VARCHAR(200) | | 대화방 제목 |
| room_type | VARCHAR(50) | DEFAULT 'travel_chat' | 대화방 유형 |
| status | VARCHAR(20) | DEFAULT 'active' | 대화방 상태 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |
| updated_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 수정일시 |

### chat_messages
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | BIGSERIAL | PRIMARY KEY | 메시지 고유 ID |
| room_id | BIGINT | NOT NULL REFERENCES chat_rooms(id) | 대화방 ID |
| sender_type | VARCHAR(20) | NOT NULL | 발신자 타입 (user, assistant) |
| content | TEXT | NOT NULL | 메시지 내용 |
| message_type | VARCHAR(50) | DEFAULT 'text' | 메시지 타입 (text, image, etc) |
| metadata | JSONB | | 메시지 메타데이터 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |

## 1.3 기준 정보

### countries
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| code | VARCHAR(3) | PRIMARY KEY | 국가 코드 (ISO 3166-1 alpha-3) |
| name_ko | VARCHAR(100) | NOT NULL | 한글 국가명 |
| name_en | VARCHAR(100) | NOT NULL | 영문 국가명 |
| flag_emoji | VARCHAR(10) | | 국기 이모지 |

---

# 🔄 2. 프론트가 알면 좋은 내부 스키마 (API 참고용)

## 2.1 사용자 설정 및 관리

### user_settings
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| user_id | BIGINT | PRIMARY KEY REFERENCES users(id) | 사용자 ID |
| notification_enabled | BOOLEAN | DEFAULT TRUE | 알림 활성화 여부 |
| language | VARCHAR(10) | DEFAULT 'ko' | 언어 설정 |
| settings | JSONB | DEFAULT '{}' | 기타 설정값 |
| updated_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 수정일시 |

### user_feedback
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | BIGSERIAL | PRIMARY KEY | 피드백 고유 ID |
| user_id | BIGINT | REFERENCES users(id) | 사용자 ID |
| feedback_type | VARCHAR(50) | NOT NULL | 피드백 타입 (bug, suggestion, complaint) |
| subject | VARCHAR(200) | | 제목 |
| content | TEXT | NOT NULL | 피드백 내용 |
| rating | INTEGER CHECK (rating >= 1 AND rating <= 5) | | 평점 (1-5) |
| status | VARCHAR(20) | DEFAULT 'pending' | 처리 상태 (pending, resolved, closed) |
| admin_response | TEXT | | 관리자 응답 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |

### message_feedback
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | BIGSERIAL | PRIMARY KEY | 피드백 고유 ID |
| user_id | BIGINT | NOT NULL REFERENCES users(id) | 사용자 ID |
| message_id | BIGINT | NOT NULL REFERENCES chat_messages(id) | 메시지 ID |
| feedback_type | VARCHAR(20) | NOT NULL | 피드백 타입 (helpful, not_helpful) |
| rating | INTEGER CHECK (rating >= 1 AND rating <= 5) | | 평점 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |

## 2.2 시스템 운영 정보

### system_notifications
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | SERIAL | PRIMARY KEY | 공지 고유 ID |
| title | VARCHAR(200) | NOT NULL | 공지 제목 |
| content | TEXT | NOT NULL | 공지 내용 |
| notification_type | VARCHAR(50) | NOT NULL | 공지 타입 (maintenance, update, notice) |
| priority | VARCHAR(20) | DEFAULT 'normal' | 우선순위 (low, normal, high, critical) |
| is_active | BOOLEAN | DEFAULT TRUE | 활성화 여부 |
| display_from | TIMESTAMP WITH TIME ZONE | | 표시 시작 시간 |
| display_until | TIMESTAMP WITH TIME ZONE | | 표시 종료 시간 |
| created_by | VARCHAR(100) | | 작성자 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |

### system_configs
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| key | VARCHAR(100) | PRIMARY KEY | 설정 키 |
| value | TEXT | | 설정 값 |
| description | TEXT | | 설정 설명 |
| updated_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 수정일시 |

---

# 🔒 3. 완전 내부 전용 스키마 (백엔드 전용)

## 3.1 인증 및 세션 관리

### phone_verification_codes
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | BIGSERIAL | PRIMARY KEY | 인증코드 고유 ID |
| phone_number_hash | VARCHAR(64) | NOT NULL | 전화번호 해시값 |
| code | VARCHAR(10) | NOT NULL | 인증 코드 |
| expires_at | TIMESTAMP WITH TIME ZONE | NOT NULL | 만료일시 |
| verified | BOOLEAN | DEFAULT FALSE | 인증 완료 여부 |
| attempt_count | INTEGER | DEFAULT 0 | 시도 횟수 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |

### user_sessions
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | BIGSERIAL | PRIMARY KEY | 세션 고유 ID |
| user_id | BIGINT | NOT NULL REFERENCES users(id) | 사용자 ID |
| token_hash | VARCHAR(64) | NOT NULL UNIQUE | 토큰 해시값 |
| expires_at | TIMESTAMP WITH TIME ZONE | NOT NULL | 만료일시 |
| device_info | JSONB | | 디바이스 정보 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |

## 3.2 LLM 기본 관리

### llm_providers
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | SERIAL | PRIMARY KEY | 제공업체 고유 ID |
| provider_name | VARCHAR(50) | NOT NULL UNIQUE | 제공업체명 (openai, anthropic 등) |
| display_name | VARCHAR(100) | NOT NULL | 표시명 |
| api_base_url | VARCHAR(200) | | API 기본 URL |
| status | VARCHAR(20) | DEFAULT 'active' | 상태 (active, inactive) |
| priority_order | INTEGER | DEFAULT 100 | 우선순위 (숫자 낮을수록 우선) |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |
| updated_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 수정일시 |

### llm_api_keys
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | SERIAL | PRIMARY KEY | 키 고유 ID |
| provider_id | INTEGER | NOT NULL REFERENCES llm_providers(id) | 제공업체 ID |
| key_name | VARCHAR(100) | NOT NULL | 키 이름/별칭 |
| api_key_encrypted | TEXT | NOT NULL | 암호화된 API 키 |
| key_status | VARCHAR(20) | DEFAULT 'active' | 키 상태 (active, inactive) |
| monthly_budget_usd | DECIMAL(10,2) | | 월 예산 (USD) |
| current_usage_usd | DECIMAL(10,2) | DEFAULT 0 | 현재 사용량 (USD) |
| last_used_at | TIMESTAMP WITH TIME ZONE | | 마지막 사용 시간 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |
| updated_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 수정일시 |

### llm_models
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | SERIAL | PRIMARY KEY | 모델 설정 ID |
| provider_id | INTEGER | NOT NULL REFERENCES llm_providers(id) | 제공업체 ID |
| model_name | VARCHAR(100) | NOT NULL | 모델명 |
| display_name | VARCHAR(100) | NOT NULL | 표시명 |
| is_available | BOOLEAN | DEFAULT TRUE | 사용 가능 여부 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |

## 3.3 Admin 관리

### admin_users
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | BIGSERIAL | PRIMARY KEY | 어드민 사용자 고유 ID |
| username | VARCHAR(50) | NOT NULL UNIQUE | 사용자명 |
| password_hash | VARCHAR(255) | NOT NULL | 암호화된 비밀번호 |
| email | VARCHAR(255) | | 이메일 |
| role | VARCHAR(50) | DEFAULT 'admin' | 권한 역할 |
| status | VARCHAR(20) | DEFAULT 'active' | 상태 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |

---

# 📊 4. 로깅 및 모니터링 (기본)

## 4.1 LLM 사용 로그

### llm_conversations_log
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | BIGSERIAL | PRIMARY KEY | 로그 고유 ID |
| request_id | VARCHAR(100) | NOT NULL | 요청 추적 ID |
| user_id | BIGINT | | 사용자 ID |
| room_id | BIGINT | | 대화방 ID |
| message_id | BIGINT | | 메시지 ID |
| llm_provider | VARCHAR(50) | NOT NULL | LLM 제공업체 |
| model_name | VARCHAR(100) | NOT NULL | 모델명 |
| prompt_tokens | INTEGER | | 입력 토큰 수 |
| completion_tokens | INTEGER | | 출력 토큰 수 |
| total_tokens | INTEGER | | 총 토큰 수 |
| duration_seconds | DOUBLE PRECISION | | 응답 시간 |
| status | VARCHAR(20) | NOT NULL | 성공/실패 상태 |
| error_message | TEXT | | 오류 메시지 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |

### llm_daily_usage
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | SERIAL | PRIMARY KEY | 사용량 ID |
| usage_date | DATE | NOT NULL | 사용 날짜 |
| provider_name | VARCHAR(50) | NOT NULL | 제공업체명 |
| model_name | VARCHAR(100) | NOT NULL | 모델명 |
| total_requests | INTEGER | DEFAULT 0 | 총 요청 수 |
| total_tokens | BIGINT | DEFAULT 0 | 총 토큰 수 |
| estimated_cost_usd | DECIMAL(10,4) | DEFAULT 0 | 예상 비용 (USD) |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |

## 4.2 기본 활동 로그

### user_activity_logs
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | BIGSERIAL | PRIMARY KEY | 로그 고유 ID |
| user_id | BIGINT | | 사용자 ID |
| activity_type | VARCHAR(50) | NOT NULL | 활동 유형 (login, message_send, room_create) |
| resource_id | BIGINT | | 리소스 ID |
| ip_address | INET | | IP 주소 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |

### error_logs
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | BIGSERIAL | PRIMARY KEY | 로그 고유 ID |
| error_id | VARCHAR(100) | NOT NULL | 오류 추적 ID |
| severity | VARCHAR(20) | NOT NULL | 심각도 (critical, error, warning) |
| component | VARCHAR(100) | NOT NULL | 오류 발생 컴포넌트 |
| error_message | TEXT | NOT NULL | 오류 메시지 |
| user_id | BIGINT | | 관련 사용자 ID |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |

## 4.3 기본 통계

### daily_stats
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | SERIAL | PRIMARY KEY | 통계 고유 ID |
| collection_date | DATE | NOT NULL UNIQUE | 수집 날짜 |
| active_users | INTEGER | NOT NULL | 일일 활성 사용자 |
| new_users | INTEGER | NOT NULL | 신규 가입자 |
| total_conversations | INTEGER | NOT NULL | 총 대화 수 |
| total_messages | INTEGER | NOT NULL | 총 메시지 수 |
| llm_requests | INTEGER | NOT NULL | LLM 요청 수 |
| total_tokens_used | BIGINT | NOT NULL | 총 토큰 사용량 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |

---

# 🌐 7. 외부 시스템 연동 스키마 (Future Work - 예약됨)

*이 섹션은 향후 기존 시스템과의 연동을 위해 설계된 스키마입니다. POC 단계에서는 구현하지 않습니다.*

## 7.1 외부 시스템 정의 및 관리

### external_systems
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | SERIAL | PRIMARY KEY | 외부 시스템 고유 ID |
| system_name | VARCHAR(50) | NOT NULL UNIQUE | 시스템 식별명 (예: telecom_customer_db) |
| display_name | VARCHAR(100) | NOT NULL | 시스템 표시명 |
| system_type | VARCHAR(50) | NOT NULL | 시스템 타입 (customer_db, crm, billing) |
| api_config | JSONB | NOT NULL | API 설정 (base_url, auth_type, endpoints 등) |
| credential_config | JSONB | | 인증 설정 (credential 요청 방식 등) |
| is_active | BOOLEAN | DEFAULT TRUE | 활성화 여부 |
| priority_order | INTEGER | DEFAULT 100 | 우선순위 |
| reserved_config_1 | JSONB | | 예약된 설정 필드 1 |
| reserved_config_2 | JSONB | | 예약된 설정 필드 2 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |
| updated_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 수정일시 |

### external_system_endpoints
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | SERIAL | PRIMARY KEY | 엔드포인트 고유 ID |
| system_id | INTEGER | NOT NULL REFERENCES external_systems(id) | 외부 시스템 ID |
| endpoint_name | VARCHAR(100) | NOT NULL | 엔드포인트 식별명 |
| endpoint_url | VARCHAR(500) | NOT NULL | 엔드포인트 URL |
| http_method | VARCHAR(10) | DEFAULT 'POST' | HTTP 메소드 |
| request_config | JSONB | | 요청 설정 (헤더, 바디 템플릿 등) |
| response_config | JSONB | | 응답 설정 (파싱 규칙 등) |
| timeout_seconds | INTEGER | DEFAULT 30 | 타임아웃 (초) |
| retry_count | INTEGER | DEFAULT 3 | 재시도 횟수 |
| is_active | BOOLEAN | DEFAULT TRUE | 활성화 여부 |
| reserved_field_1 | TEXT | | 예약된 필드 1 |
| reserved_field_2 | JSONB | | 예약된 필드 2 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |
| updated_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 수정일시 |

## 7.2 사용자별 연동 상태 관리

### user_external_integrations
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | BIGSERIAL | PRIMARY KEY | 연동 상태 고유 ID |
| user_id | BIGINT | NOT NULL REFERENCES users(id) | 사용자 ID |
| system_id | INTEGER | NOT NULL REFERENCES external_systems(id) | 외부 시스템 ID |
| unlock_status | VARCHAR(20) | DEFAULT 'locked' | 연동 상태 (locked, unlocked, pending, expired) |
| external_user_id | VARCHAR(100) | | 외부 시스템의 사용자 ID (암호화 저장) |
| unlock_metadata | JSONB | | 연동 관련 메타데이터 |
| unlock_conditions | JSONB | | 연동 해제 조건 |
| verification_data | JSONB | | 검증 데이터 (해시값 등) |
| last_verified_at | TIMESTAMP WITH TIME ZONE | | 마지막 검증 시간 |
| expires_at | TIMESTAMP WITH TIME ZONE | | 연동 만료 시간 |
| auto_renewal | BOOLEAN | DEFAULT FALSE | 자동 갱신 여부 |
| reserved_status | VARCHAR(50) | | 예약된 상태 필드 |
| reserved_metadata | JSONB | | 예약된 메타데이터 필드 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |
| updated_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 수정일시 |

**인덱스:**
```sql
UNIQUE(user_id, system_id)
INDEX(unlock_status)
INDEX(expires_at)
```

## 7.3 1회성 데이터 세션 관리

### external_data_sessions
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | BIGSERIAL | PRIMARY KEY | 세션 고유 ID |
| session_uuid | UUID | NOT NULL UNIQUE DEFAULT gen_random_uuid() | 세션 UUID |
| user_id | BIGINT | NOT NULL REFERENCES users(id) | 사용자 ID |
| system_id | INTEGER | NOT NULL REFERENCES external_systems(id) | 외부 시스템 ID |
| integration_id | BIGINT | NOT NULL REFERENCES user_external_integrations(id) | 연동 상태 ID |
| session_type | VARCHAR(50) | NOT NULL | 세션 타입 (credential_request, data_fetch) |
| status | VARCHAR(20) | DEFAULT 'active' | 세션 상태 (active, completed, expired, failed) |
| purpose | VARCHAR(100) | | 세션 목적 (여행추천, 요금조회 등) |
| request_context | JSONB | | 요청 컨텍스트 |
| credential_token | VARCHAR(500) | | 일회성 credential 토큰 (암호화) |
| data_types_requested | TEXT[] | | 요청한 데이터 타입들 |
| processing_status | VARCHAR(20) | | 처리 상태 (pending, processing, completed) |
| expires_at | TIMESTAMP WITH TIME ZONE | NOT NULL | 세션 만료 시간 (기본: 10분) |
| completed_at | TIMESTAMP WITH TIME ZONE | | 완료 시간 |
| reserved_token | TEXT | | 예약된 토큰 필드 |
| reserved_context | JSONB | | 예약된 컨텍스트 필드 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |
| updated_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 수정일시 |

**주의사항:**
- 실제 외부 데이터는 이 테이블에 저장하지 않음 (메모리에서만 처리)
- 짧은 만료시간 설정 (기본 10분)
- 자동 정리 작업 필요

**인덱스:**
```sql
INDEX(session_uuid)
INDEX(user_id, system_id)
INDEX(status, expires_at)
```

## 7.4 외부 API 호출 감사 로그

### external_api_calls
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | BIGSERIAL | PRIMARY KEY | 로그 고유 ID |
| call_uuid | UUID | NOT NULL DEFAULT gen_random_uuid() | 호출 추적 UUID |
| session_id | BIGINT | REFERENCES external_data_sessions(id) | 관련 세션 ID |
| user_id | BIGINT | NOT NULL REFERENCES users(id) | 사용자 ID |
| system_id | INTEGER | NOT NULL REFERENCES external_systems(id) | 외부 시스템 ID |
| endpoint_id | INTEGER | REFERENCES external_system_endpoints(id) | 엔드포인트 ID |
| call_type | VARCHAR(50) | NOT NULL | 호출 타입 (credential_request, data_fetch) |
| request_method | VARCHAR(10) | NOT NULL | HTTP 메소드 |
| request_url | VARCHAR(500) | NOT NULL | 요청 URL |
| request_headers_hash | VARCHAR(64) | | 요청 헤더 해시 (개인정보 제외) |
| response_status_code | INTEGER | | 응답 상태 코드 |
| response_size_bytes | INTEGER | | 응답 크기 |
| duration_ms | INTEGER | | 응답 시간 (밀리초) |
| retry_count | INTEGER | DEFAULT 0 | 재시도 횟수 |
| success | BOOLEAN | NOT NULL | 성공 여부 |
| error_code | VARCHAR(50) | | 오류 코드 |
| error_message | TEXT | | 오류 메시지 (개인정보 제외) |
| rate_limit_info | JSONB | | Rate Limit 정보 |
| reserved_metrics | JSONB | | 예약된 메트릭 필드 |
| reserved_status | VARCHAR(50) | | 예약된 상태 필드 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |

**보안 정책:**
- 개인정보는 절대 저장하지 않음
- 요청/응답 내용은 해시값만 저장
- 에러 메시지에서 개인정보 필터링

**인덱스:**
```sql
INDEX(call_uuid)
INDEX(user_id, system_id, created_at)
INDEX(success, created_at)
INDEX(error_code) WHERE error_code IS NOT NULL
```

### external_data_access_audit
| 컬럼명 | 타입 | 제약조건 | 설명 |
|--------|------|----------|------|
| id | BIGSERIAL | PRIMARY KEY | 감사 로그 고유 ID |
| user_id | BIGINT | NOT NULL REFERENCES users(id) | 사용자 ID |
| system_id | INTEGER | NOT NULL REFERENCES external_systems(id) | 외부 시스템 ID |
| session_id | BIGINT | REFERENCES external_data_sessions(id) | 세션 ID |
| access_type | VARCHAR(50) | NOT NULL | 접근 타입 (view, use, process) |
| data_categories | TEXT[] | | 접근한 데이터 카테고리들 |
| purpose | VARCHAR(100) | NOT NULL | 사용 목적 |
| processing_result | VARCHAR(50) | | 처리 결과 (success, partial, failed) |
| data_retention_policy | VARCHAR(50) | | 데이터 보존 정책 (immediate_delete, temp_cache) |
| compliance_flags | JSONB | | 컴플라이언스 관련 플래그 |
| consent_version | VARCHAR(20) | | 동의서 버전 |
| ip_address | INET | | 접근 IP |
| user_agent_hash | VARCHAR(64) | | User Agent 해시 |
| reserved_audit_1 | TEXT | | 예약된 감사 필드 1 |
| reserved_audit_2 | JSONB | | 예약된 감사 필드 2 |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT CURRENT_TIMESTAMP | 생성일시 |

**인덱스:**
```sql
INDEX(user_id, created_at)
INDEX(system_id, access_type, created_at)
INDEX(purpose)
```

---

# 📊 5. 권장 인덱스 (POC용)

## 5.1 기본 성능 인덱스

### 사용자 관련
```sql
CREATE INDEX idx_users_phone_hash ON users (phone_number_hash);
CREATE INDEX idx_users_status ON users (status) WHERE status = 'active';
```

### 대화 관련
```sql
CREATE INDEX idx_chat_rooms_user_id ON chat_rooms (user_id);
CREATE INDEX idx_chat_messages_room_id ON chat_messages (room_id);
CREATE INDEX idx_chat_messages_created ON chat_messages (room_id, created_at DESC);
```

### 로그 관련
```sql
CREATE INDEX idx_activity_logs_user_created ON user_activity_logs (user_id, created_at);
CREATE INDEX idx_llm_logs_created ON llm_conversations_log (created_at);
```

### JSONB 필드
```sql
CREATE INDEX idx_chat_messages_metadata ON chat_messages USING GIN (metadata);
CREATE INDEX idx_user_settings_settings ON user_settings USING GIN (settings);
```

## 5.2 외부 연동 관련 인덱스 (Future Work)

### 연동 상태 관련
```sql
CREATE UNIQUE INDEX idx_user_external_unique ON user_external_integrations (user_id, system_id);
CREATE INDEX idx_user_external_status ON user_external_integrations (unlock_status);
CREATE INDEX idx_user_external_expires ON user_external_integrations (expires_at) WHERE expires_at IS NOT NULL;
```

### 세션 관리 관련
```sql
CREATE INDEX idx_external_sessions_uuid ON external_data_sessions (session_uuid);
CREATE INDEX idx_external_sessions_user_system ON external_data_sessions (user_id, system_id);
CREATE INDEX idx_external_sessions_cleanup ON external_data_sessions (status, expires_at);
```

### API 호출 로그 관련
```sql
CREATE INDEX idx_external_calls_uuid ON external_api_calls (call_uuid);
CREATE INDEX idx_external_calls_session ON external_api_calls (session_id) WHERE session_id IS NOT NULL;
CREATE INDEX idx_external_calls_performance ON external_api_calls (system_id, success, created_at);
```

---

# 📝 8. 구현 우선순위

## Phase 1: 핵심 기능 (POC)
1. **업체 공유 스키마** 전체 (1.1 ~ 1.3)
2. **기본 사용자 설정** (2.1 일부)
3. **인증/세션** (3.1)
4. **기본 LLM 관리** (3.2)

## Phase 2: 운영 기능 (POC)
1. **Admin 관리** (3.3)
2. **시스템 공지** (2.2)
3. **기본 로깅** (4.1 ~ 4.2)
4. **피드백 시스템** (2.1 나머지)

## Phase 3: 모니터링 (POC)
1. **상세 로깅** (4.1 ~ 4.3 전체)
2. **성능 최적화** 인덱스 추가
3. **통계 수집** 기능

## Phase 4: 외부 연동 준비 (Future Work)
1. **외부 시스템 정의** (7.1) - 기본 스키마 생성
2. **연동 상태 관리** (7.2) - 사용자별 unlock 관리
3. **세션 관리 시스템** (7.3) - 1회성 데이터 처리
4. **감사 로그 시스템** (7.4) - 보안 및 컴플라이언스

## Phase 5: 외부 연동 구현 (Future Work)
1. **API 클라이언트** 구현
2. **Credential 요청/관리** 시스템
3. **데이터 처리 파이프라인** 구현
4. **자동 정리** 및 **모니터링** 시스템

---

# 🔧 9. 데이터 보존 정책 (Future Work)

## 9.1 외부 데이터 처리 원칙
- **즉시 삭제**: 외부에서 가져온 개인정보는 처리 완료 즉시 삭제
- **로그만 보존**: 개인정보를 제외한 호출 이력과 성능 메트릭만 보존
- **단기 세션**: 모든 외부 데이터 세션은 최대 10분 만료
- **자동 정리**: 만료된 세션과 토큰의 자동 정리 작업

## 9.2 컴플라이언스 고려사항
- **GDPR/CCPA 준수**: 개인정보 처리 최소화
- **동의 관리**: 외부 데이터 사용에 대한 명시적 동의
- **감사 추적**: 모든 외부 데이터 접근 이력 보존
- **데이터 주체 권리**: 삭제 요청 시 관련 모든 데이터 정리

---

이 POC용 DB 스키마는 핵심 채팅 기능과 기본적인 관리 기능에 집중하여 설계되었으며, 향후 외부 시스템 연동을 위한 확장 가능한 구조를 포함하고 있습니다.